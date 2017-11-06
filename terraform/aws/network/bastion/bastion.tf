#--------------------------------------------------------------
# This module creates all resources necessary for a Bastion
# host
#--------------------------------------------------------------

variable "enabled" {}
variable "name" {}

variable "vpc_id" {}
variable "public_subnet_tier" {}

variable "key_name" {}
variable "instance_type" {}

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

# http://docs.aws.amazon.com/quickstart/latest/linux-bastion/welcome.html
resource "aws_cloudformation_stack" "bastion" {
  count        = "${var.enabled == "true" ? 1 : 0}"
  name         = "${var.name}-stack"
  capabilities = ["CAPABILITY_IAM"]

  parameters {
    AvailabilityZones   = "${data.aws_subnet.public.0.availability_zone},${data.aws_subnet.public.1.availability_zone}"
    BastionAMIOS        = "Amazon-Linux-HVM"
    BastionInstanceType = "${var.instance_type}"
    KeyPairName         = "${var.key_name}"
    NumBastionHosts     = "1"
    PublicSubnet1ID     = "${data.aws_subnet.public.0.id}"
    PublicSubnet2ID     = "${data.aws_subnet.public.1.id}"
    RemoteAccessCIDR    = "0.0.0.0/0"
    VPCID               = "${data.aws_vpc.selected.id}"
  }

  template_body = "${file("${path.module}/linux-bastion-master.template")}"
}

resource "aws_security_group" "empty" {
  name_prefix = "${var.name}-empty-sg-"
  description = "Empty SG for use when bastion stack is disabled"
  vpc_id      = "${data.aws_vpc.selected.id}"
}

data "template_file" "eip" {
  count    = "${var.enabled == "true" ? 1 : 0}"
  template = "$${eip}"

  vars {
    eip = "${aws_cloudformation_stack.bastion.outputs["EIP"]}"
  }
}

data "template_file" "sg" {
  count    = "${var.enabled == "true" ? 1 : 0}"
  template = "$${sg}"

  vars {
    sg = "${aws_cloudformation_stack.bastion.outputs["BastionSecurityGroupID"]}"
  }
}

output "user" {
  value = "ec2-user"
}

output "public_ip" {
  value = "${var.enabled == "true" ? join("", data.template_file.eip.*.rendered) : "0.0.0.0"}"
}

output "security_group_id" {
  value = "${var.enabled == "true" ? join("", data.template_file.sg.*.rendered) : aws_security_group.empty.id}"
}

output "ingress_cidr" {
  value = "0.0.0.0/0"
}
