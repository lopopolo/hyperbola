#--------------------------------------------------------------
# This module creates all networking resources
#--------------------------------------------------------------

variable "name" {}

variable "vpc_cidr" {}

variable "azs" {}

variable "region" {}

variable "private_subnets" {}

variable "public_subnets" {}

variable "key_name" {}

variable "bastion_instance_type" {}

module "vpc" {
  source = "./vpc"

  name = "${var.name}-vpc"
  cidr = "${var.vpc_cidr}"
}

module "public_subnet" {
  source = "./public_subnet"

  name   = "${var.name}-public"
  vpc_id = "${module.vpc.vpc_id}"
  cidrs  = "${var.public_subnets}"
  azs    = "${var.azs}"
}

module "private_subnet" {
  source = "./private_subnet"

  name   = "${var.name}-private"
  vpc_id = "${module.vpc.vpc_id}"
  cidrs  = "${var.private_subnets}"
  azs    = "${var.azs}"

  nat_gateway_ids = "${module.nat.nat_gateway_ids}"
}

module "bastion" {
  source = "./bastion"

  name               = "${var.name}-bastion"
  vpc_id             = "${module.vpc.vpc_id}"
  public_subnet_name = "${module.public_subnet.tag_value}"
  key_name           = "${var.key_name}"
  instance_type      = "${var.bastion_instance_type}"
}

module "nat" {
  source = "./nat"

  name               = "${var.name}-nat"
  vpc_id             = "${module.vpc.vpc_id}"
  public_subnet_name = "${module.public_subnet.tag_value}"
}

resource "aws_network_acl" "acl" {
  vpc_id     = "${module.vpc.vpc_id}"
  subnet_ids = ["${concat(split(",", module.public_subnet.subnet_ids), split(",", module.private_subnet.subnet_ids))}"]

  ingress {
    protocol   = "-1"
    rule_no    = 100
    action     = "allow"
    cidr_block = "0.0.0.0/0"
    from_port  = 0
    to_port    = 0
  }

  egress {
    protocol   = "-1"
    rule_no    = 100
    action     = "allow"
    cidr_block = "0.0.0.0/0"
    from_port  = 0
    to_port    = 0
  }

  tags {
    Name = "${var.name}-all"
  }
}

# VPC
output "vpc_id" {
  value = "${module.vpc.vpc_id}"
}

output "vpc_cidr" {
  value = "${module.vpc.vpc_cidr}"
}

# Subnets
output "public_subnet_name" {
  value = "${module.public_subnet.tag_value}"
}

output "private_subnet_name" {
  value = "${module.private_subnet.tag_value}"
}

# Bastion
output "bastion_user" {
  value = "${module.bastion.user}"
}

output "bastion_public_ip" {
  value = "${module.bastion.public_ip}"
}

output "bastion_security_group_id" {
  value = "${module.bastion.security_group_id}"
}

output "bastion_ingress_cidr" {
  value = "${module.bastion.ingress_cidr}"
}

# NAT
output "nat_gateway_ids" {
  value = "${module.nat.nat_gateway_ids}"
}
