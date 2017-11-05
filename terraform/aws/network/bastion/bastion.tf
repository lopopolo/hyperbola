#--------------------------------------------------------------
# This module creates all resources necessary for a Bastion
# host
#--------------------------------------------------------------

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

output "user" {
  value = "ec2-user"
}

output "public_ip" {
  value = "${aws_cloudformation_stack.bastion.outputs["EIP"]}"
}

output "security_group_id" {
  value = "${aws_cloudformation_stack.bastion.outputs["BastionSecurityGroupID"]}"
}

output "ingress_cidr" {
  value = "0.0.0.0/0"
}
