#--------------------------------------------------------------
# This module creates all resources necessary for a Bastion
# host
#--------------------------------------------------------------

variable "name" {
  default = "bastion"
}

variable "vpc_id" {}

variable "vpc_cidr" {}

variable "region" {}

variable "public_subnet_ids" {}

variable "key_name" {}

variable "instance_type" {}

resource "aws_security_group" "bastion" {
  name        = "${var.name}"
  vpc_id      = "${var.vpc_id}"
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
    cidr_blocks = ["${var.vpc_cidr}"]
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

module "ami" {
  source        = "github.com/terraform-community-modules/tf_aws_ubuntu_ami/ebs"
  instance_type = "${var.instance_type}"
  region        = "${var.region}"
  distribution  = "trusty"
}

resource "aws_iam_instance_profile" "bastion" {
  name  = "test_profile"
  roles = ["${aws_iam_role.bastion.name}"]
}

resource "aws_iam_role" "bastion" {
  name = "bastion"

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
  name = "bastion"
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

resource "aws_launch_configuration" "bastion" {
  name_prefix          = "${var.name}-"
  image_id             = "${module.ami.ami_id}"
  instance_type        = "${var.instance_type}"
  user_data            = "${file("${path.module}/user-data.sh")}"
  key_name             = "${var.key_name}"
  security_groups      = ["${aws_security_group.bastion.id}"]
  iam_instance_profile = "${aws_iam_instance_profile.bastion.name}"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "bastion" {
  name                      = "${aws_launch_configuration.bastion.name}"
  vpc_zone_identifier       = ["${split(",", var.public_subnet_ids)}"]
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

output "security_group_id" {
  value = "${aws_security_group.bastion.id}"
}
