variable "name" {}

variable "region" {}

variable "vpc_id" {}

variable "vpc_cidr" {}

variable "key_name" {}

variable "azs" {}

variable "private_subnet_ids" {}

variable "public_subnet_ids" {}

variable "instance_type" {
  default = "t2.small"
}

resource "aws_security_group" "elb" {
  name        = "${var.name}.elb"
  vpc_id      = "${var.vpc_id}"
  description = "Security group for Nodejs ELB"

  tags {
    Name = "${var.name}-elb"
  }

  lifecycle {
    create_before_destroy = true
  }

  ingress {
    protocol    = "tcp"
    from_port   = 80
    to_port     = 80
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    protocol    = "tcp"
    from_port   = 443
    to_port     = 443
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    protocol        = "tcp"
    from_port       = 80
    to_port         = 80
    security_groups = ["${aws_security_group.backend.id}"]
  }

  egress {
    protocol        = "tcp"
    from_port       = 443
    to_port         = 443
    security_groups = ["${aws_security_group.backend.id}"]
  }
}

resource "aws_elb" "elb" {
  name                        = "${var.name}-elb"
  connection_draining         = true
  connection_draining_timeout = 400

  subnets         = ["${split(",", var.public_subnet_ids)}"]
  security_groups = ["${aws_security_group.elb.id}"]

  lifecycle {
    create_before_destroy = true
  }

  listener {
    lb_port           = 80
    lb_protocol       = "tcp"
    instance_port     = 80
    instance_protocol = "tcp"
  }

  listener {
    lb_port           = 443
    lb_protocol       = "tcp"
    instance_port     = 443
    instance_protocol = "tcp"
  }

  health_check {
    healthy_threshold   = 2
    unhealthy_threshold = 3
    timeout             = 10
    interval            = 15
    target              = "HTTP:80/ping"
  }
}

resource "template_file" "user_data" {
  template = "${file("${path.module}/provision.sh.tpl")}"

  lifecycle {
    create_before_destroy = true
  }

  vars {
    ansible_vault_password = "${replace(file("${path.root}/../.secrets/vault-password.txt"), "\n", "")}"
  }
}

module "ami" {
  source        = "github.com/terraform-community-modules/tf_aws_ubuntu_ami/ebs"
  instance_type = "${var.instance_type}"
  region        = "${var.region}"
  distribution  = "xenial"
  storagetype   = "ebs-ssd"
}

resource "aws_launch_configuration" "backend" {
  name_prefix     = "${var.name}-"
  image_id        = "${module.ami.ami_id}"
  instance_type   = "${var.instance_type}"
  key_name        = "${var.key_name}"
  security_groups = ["${aws_security_group.backend.id}"]
  user_data       = "${template_file.user_data.rendered}"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "backend" {
  name                  = "${aws_launch_configuration.backend.name}"
  launch_configuration  = "${aws_launch_configuration.backend.name}"
  desired_capacity      = "1"
  min_size              = "1"
  max_size              = "1"
  wait_for_elb_capacity = "1"

  # provisioning takes up to 15 minutes
  # TODO: remove when we switch to prebaking images with packer
  wait_for_capacity_timeout = "30m"

  availability_zones  = ["${split(",", var.azs)}"]
  vpc_zone_identifier = ["${split(",", var.private_subnet_ids)}"]
  load_balancers      = ["${aws_elb.elb.id}"]

  lifecycle {
    create_before_destroy = true
  }

  tag {
    key                 = "Name"
    value               = "${var.name}"
    propagate_at_launch = true
  }
}

output "elb_zone_id" {
  value = "${aws_elb.elb.zone_id}"
}

output "private_fqdn" {
  value = "${aws_route53_record.wiki.fqdn}"
}

output "elb_dns" {
  value = "${aws_elb.elb.dns_name}"
}
