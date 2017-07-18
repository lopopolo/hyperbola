variable "name" {}
variable "env" {}

variable "vpc_id" {}
variable "public_subnet_tier" {}
variable "private_subnet_tier" {}

variable "key_name" {}

variable "instance_type" {
  default = "t2.micro"
}

variable "size" {
  default = "1"
}

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
  name_prefix = "${var.env}-alb-"
  vpc_id      = "${data.aws_vpc.selected.id}"
  description = "Security group for ${var.name} ALB"

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
    Name = "${var.name}-alb-sg"
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_alb" "alb" {
  name     = "${var.env}-alb"
  internal = false

  subnets         = ["${data.aws_subnet.public.*.id}"]
  security_groups = ["${aws_security_group.alb.id}"]
  ip_address_type = "dualstack"

  lifecycle {
    create_before_destroy = true
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
  name     = "${var.env}-alb-tg"
  port     = 80
  protocol = "HTTP"
  vpc_id   = "${data.aws_vpc.selected.id}"

  deregistration_delay = 30

  health_check {
    path = "/healthz" # runs a request through nginx to rack
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
}

resource "aws_launch_configuration" "backend" {
  name_prefix     = "${var.name}-"
  image_id        = "${data.aws_ami.backend.id}"
  instance_type   = "${var.instance_type}"
  key_name        = "${var.key_name}"
  security_groups = ["${aws_security_group.backend.id}"]

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "backend" {
  name                  = "${aws_launch_configuration.backend.name}"
  launch_configuration  = "${aws_launch_configuration.backend.name}"
  desired_capacity      = "${var.size}"
  min_size              = "${var.size}"
  max_size              = "${var.size}"
  wait_for_elb_capacity = "${var.size}"

  availability_zones  = ["${data.aws_subnet.private.*.availability_zone}"]
  vpc_zone_identifier = ["${data.aws_subnet.private.*.id}"]
  target_group_arns   = ["${aws_alb_target_group.backend.arn}"]

  lifecycle {
    create_before_destroy = true
  }

  tag {
    key                 = "Name"
    value               = "${var.name}"
    propagate_at_launch = true
  }

  depends_on = [
    "aws_security_group_rule.backend-to-mysql",
    "aws_security_group_rule.mysql-from-backend",
    "aws_security_group_rule.backend-to-redis",
    "aws_security_group_rule.redis-from-backend",
  ]
}

output "alb_zone_id" {
  value = "${aws_alb.alb.zone_id}"
}

output "alb_dns" {
  value = "${aws_alb.alb.dns_name}"
}
