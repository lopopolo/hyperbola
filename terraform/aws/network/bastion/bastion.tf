#--------------------------------------------------------------
# This module creates all resources necessary for a Bastion
# host
#--------------------------------------------------------------

variable "name" {}

variable "vpc_id" {}
variable "public_subnet_name" {}

variable "key_name" {}

variable "instance_type" {}

data "aws_vpc" "selected" {
  id = "${var.vpc_id}"
}

data "aws_subnet_ids" "public" {
  vpc_id = "${data.aws_vpc.selected.id}"

  tags {
    Network = "${var.public_subnet_name}"
  }
}

resource "aws_security_group" "bastion" {
  name        = "${var.name}"
  vpc_id      = "${data.aws_vpc.selected.id}"
  description = "Bastion security group"

  tags {
    Name = "${var.name}"
  }

  lifecycle {
    create_before_destroy = true
  }

  ingress {
    protocol    = -1
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["${data.aws_vpc.selected.cidr_block}"]
  }

  ingress {
    protocol    = "tcp"
    from_port   = 22
    to_port     = 22
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    protocol    = -1
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "name"
    values = ["*ubuntu-xenial-16.04-amd64-server-*"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
}

resource "aws_iam_instance_profile" "bastion" {
  name = "${var.name}-profile"
  role = "${aws_iam_role.bastion.name}"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_iam_role" "bastion" {
  name = "${var.name}-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# https://github.com/skymill/aws-ec2-assign-elastic-ip#required-iam-permissions
# as well as describe autoscaling for motd script
resource "aws_iam_role_policy" "bastion" {
  name = "${var.name}-policy"
  role = "${aws_iam_role.bastion.id}"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:AssociateAddress",
        "ec2:Describe*",
        "autoscaling:Describe*"
      ],
      "Resource": "*"
    }
  ]
}
EOF
}

resource "aws_eip" "bastion" {
  vpc = true

  lifecycle {
    create_before_destroy = true
  }
}

data "aws_route53_zone" "aws-dc" {
  name         = "aws.hyperboladc.net."
  private_zone = false
}

resource "aws_route53_record" "aws-dc" {
  zone_id = "${data.aws_route53_zone.aws-dc.zone_id}"
  name    = "${var.name}"
  type    = "A"
  ttl     = "300"
  records = ["${aws_eip.bastion.public_ip}"]
}

resource "aws_launch_configuration" "bastion" {
  name_prefix          = "${var.name}-"
  image_id             = "${data.aws_ami.ubuntu.id}"
  instance_type        = "${var.instance_type}"
  user_data            = "${file("${path.module}/bastion_init.sh")}"
  key_name             = "${var.key_name}"
  security_groups      = ["${aws_security_group.bastion.id}"]
  iam_instance_profile = "${aws_iam_instance_profile.bastion.name}"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "bastion" {
  name                      = "${aws_launch_configuration.bastion.name}"
  vpc_zone_identifier       = ["${data.aws_subnet_ids.public.ids}"]
  desired_capacity          = "1"
  min_size                  = "1"
  max_size                  = "1"
  health_check_grace_period = "60"
  health_check_type         = "EC2"
  force_delete              = false
  wait_for_capacity_timeout = 0
  launch_configuration      = "${aws_launch_configuration.bastion.name}"

  tag {
    key                 = "Name"
    value               = "${var.name}"
    propagate_at_launch = true
  }

  tag {
    key                 = "EIP"
    value               = "${aws_eip.bastion.public_ip}"
    propagate_at_launch = true
  }

  lifecycle {
    create_before_destroy = true
  }
}

output "user" {
  value = "ubuntu"
}

output "public_ip" {
  value = "${aws_eip.bastion.public_ip}"
}

output "fqdn" {
  value = "${aws_route53_record.aws-dc.fqdn}"
}

output "security_group_id" {
  value = "${aws_security_group.bastion.id}"
}

output "ingress_cidr" {
  value = "0.0.0.0/0"
}
