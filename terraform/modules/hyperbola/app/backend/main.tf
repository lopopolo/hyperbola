variable "name" {}
variable "env" {}

variable "vpc_id" {}
variable "public_subnet_tier" {}
variable "private_subnet_tier" {}

variable "key_name" {}

variable "size" {
  default = "1"
}

variable "iam_instance_profile" {}

data "aws_vpc" "selected" {
  id = "${var.vpc_id}"
}

data "aws_subnet_ids" "public" {
  vpc_id = "${data.aws_vpc.selected.id}"

  tags {
    Network = "${var.public_subnet_tier}"
  }
}

data "aws_subnet" "public" {
  count = "${length(data.aws_subnet_ids.public.ids)}"
  id    = "${data.aws_subnet_ids.public.ids[count.index]}"
}

data "aws_subnet_ids" "private" {
  vpc_id = "${data.aws_vpc.selected.id}"

  tags {
    Network = "${var.private_subnet_tier}"
  }
}

data "aws_subnet" "private" {
  count = "${length(data.aws_subnet_ids.private.ids)}"
  id    = "${data.aws_subnet_ids.private.ids[count.index]}"
}

resource "aws_security_group" "alb" {
  name_prefix = "app-alb-sg-"
  vpc_id      = "${data.aws_vpc.selected.id}"

  ingress {
    protocol         = "tcp"
    from_port        = 80
    to_port          = 80
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    protocol         = "tcp"
    from_port        = 443
    to_port          = 443
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    protocol        = "tcp"
    from_port       = 80
    to_port         = 80
    security_groups = ["${aws_security_group.backend.id}"]
  }

  egress {
    protocol        = "tcp"
    from_port       = 8888
    to_port         = 8888
    security_groups = ["${aws_security_group.backend.id}"]
  }

  tags {
    Name        = "${var.name}-alb-sg"
    Environment = "${var.env}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_alb" "alb" {
  name_prefix = "applb-"
  internal    = false

  subnets         = ["${data.aws_subnet.public.*.id}"]
  security_groups = ["${aws_security_group.alb.id}"]
  ip_address_type = "dualstack"

  lifecycle {
    create_before_destroy = true
  }

  tags {
    Name        = "${var.name}-alb"
    Environment = "${var.env}"
  }
}

data "aws_acm_certificate" "alb-cert" {
  domain   = "hyperbo.la"
  statuses = ["ISSUED"]
}

resource "aws_alb_listener" "alb-https" {
  load_balancer_arn = "${aws_alb.alb.arn}"
  port              = "443"
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-TLS-1-2-2017-01"
  certificate_arn   = "${data.aws_acm_certificate.alb-cert.arn}"

  default_action {
    target_group_arn = "${aws_alb_target_group.backend.arn}"
    type             = "forward"
  }
}

resource "aws_alb_listener" "alb-http" {
  load_balancer_arn = "${aws_alb.alb.arn}"
  port              = "80"
  protocol          = "HTTP"

  default_action {
    target_group_arn = "${aws_alb_target_group.backend.arn}"
    type             = "forward"
  }
}

resource "aws_alb_target_group" "backend" {
  name_prefix = "apptg-"
  port        = 80
  protocol    = "HTTP"
  vpc_id      = "${data.aws_vpc.selected.id}"

  deregistration_delay = 30

  health_check {
    path = "/healthz" # runs a request through nginx to the application server
    port = 8888
  }
}

data "aws_ami" "backend" {
  most_recent = true
  owners      = ["self"]

  filter {
    name   = "tag:ami"
    values = ["aws-us-west-2-hyperbola-app"]
  }

  filter {
    name   = "tag:Version"
    values = ["0.147.0"]
  }
}

resource "aws_launch_configuration" "backend" {
  name_prefix     = "app-backend-"
  image_id        = "${data.aws_ami.backend.id}"
  instance_type   = "t3.nano"
  key_name        = "${var.key_name}"
  security_groups = ["${aws_security_group.backend.id}"]

  iam_instance_profile = "${var.iam_instance_profile}"

  enable_monitoring = false    # disable 11 CloudWatch metrics per instance
  spot_price        = "0.0052"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "backend" {
  name                  = "${aws_launch_configuration.backend.name}"
  launch_configuration  = "${aws_launch_configuration.backend.name}"
  desired_capacity      = "${var.size}"
  min_size              = "${var.size}"
  max_size              = "${2 * var.size + 1}"
  wait_for_elb_capacity = "${var.size}"

  availability_zones  = ["${data.aws_subnet.private.*.availability_zone}"]
  vpc_zone_identifier = ["${data.aws_subnet.private.*.id}"]
  target_group_arns   = ["${aws_alb_target_group.backend.arn}"]

  lifecycle {
    create_before_destroy = true
  }

  tag {
    key                 = "Name"
    value               = "${var.name}-backend"
    propagate_at_launch = true
  }

  tag {
    key                 = "Environment"
    value               = "${var.env}"
    propagate_at_launch = true
  }

  tag {
    key                 = "Version"
    value               = "0.147.0"
    propagate_at_launch = true
  }

  depends_on = [
    "aws_security_group_rule.backend-to-mysql",
    "aws_security_group_rule.mysql-from-backend",
  ]
}

resource "aws_autoscaling_policy" "backend-scaleup" {
  name                   = "${var.name}-backend-scaleup-policy"
  policy_type            = "SimpleScaling"
  adjustment_type        = "ChangeInCapacity"
  scaling_adjustment     = 1
  cooldown               = 300
  autoscaling_group_name = "${aws_autoscaling_group.backend.name}"
}

resource "aws_cloudwatch_metric_alarm" "backend-cpu-scaleup" {
  alarm_name          = "${var.name}-backend-scaleup-cpu-alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = 120
  statistic           = "Average"
  threshold           = 60

  dimensions = {
    "AutoScalingGroupName" = "${aws_autoscaling_group.backend.name}"
  }

  actions_enabled = true
  alarm_actions   = ["${aws_autoscaling_policy.backend-scaleup.arn}"]
}

resource "aws_autoscaling_policy" "backend-scaledown" {
  name                   = "${var.name}-backend-scaledown-policy"
  policy_type            = "SimpleScaling"
  adjustment_type        = "ChangeInCapacity"
  scaling_adjustment     = -1
  cooldown               = 300
  autoscaling_group_name = "${aws_autoscaling_group.backend.name}"
}

resource "aws_cloudwatch_metric_alarm" "backend-cpu-scaledown" {
  alarm_name          = "${var.name}-backend-scaledown-cpu-alarm"
  comparison_operator = "LessThanOrEqualToThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = 120
  statistic           = "Average"
  threshold           = 20

  dimensions = {
    "AutoScalingGroupName" = "${aws_autoscaling_group.backend.name}"
  }

  actions_enabled = true
  alarm_actions   = ["${aws_autoscaling_policy.backend-scaledown.arn}"]
}

output "alb_zone_id" {
  value = "${aws_alb.alb.zone_id}"
}

output "alb_dns" {
  value = "${aws_alb.alb.dns_name}"
}
