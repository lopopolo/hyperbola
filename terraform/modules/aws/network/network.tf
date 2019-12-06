#--------------------------------------------------------------
# This module creates all networking resources
#--------------------------------------------------------------

variable "name" {
}

variable "vpc_cidr" {
}

variable "azs" {
}

variable "nat_enabled" {
}

variable "region" {
}

module "vpc" {
  source = "./vpc"

  name = "${var.name}-vpc"
  cidr = var.vpc_cidr
}

module "tier" {
  source = "./subnet_tier"
}

module "public_subnet" {
  source = "./public_subnet"

  name   = "${var.name}-public"
  vpc_id = module.vpc.vpc_id
  azs    = var.azs

  subnet_tier         = module.tier.public
  internet_gateway_id = module.vpc.internet_gateway_id
  egress_gateway_id   = module.vpc.egress_gateway_id
}

module "private_subnet" {
  source = "./private_subnet"

  name   = "${var.name}-private"
  vpc_id = module.vpc.vpc_id
  azs    = var.azs

  subnet_tier       = module.tier.private
  nat_enabled       = var.nat_enabled
  nat_gateway_ids   = module.nat.nat_gateway_ids
  egress_gateway_id = module.vpc.egress_gateway_id
}

module "nat" {
  source = "./nat"

  enabled            = var.nat_enabled
  name               = "${var.name}-nat"
  vpc_id             = module.vpc.vpc_id
  public_subnet_tier = module.public_subnet.tier
}

module "management" {
  source = "./management"

  name                = "${var.name}-management"
  vpc_id              = module.vpc.vpc_id
  azs                 = var.azs
  internet_gateway_id = module.vpc.internet_gateway_id
  egress_gateway_id   = module.vpc.egress_gateway_id
  s3_route_tables = concat(
    module.public_subnet.route_table,
    module.private_subnet.route_table,
  )
}

resource "aws_network_acl" "acl" {
  vpc_id = module.vpc.vpc_id

  ingress {
    protocol   = "-1"
    rule_no    = 100
    action     = "allow"
    cidr_block = "0.0.0.0/0"
    from_port  = 0
    to_port    = 0
  }

  ingress {
    protocol        = "-1"
    rule_no         = 200
    action          = "allow"
    ipv6_cidr_block = "::/0"
    from_port       = 0
    to_port         = 0
  }

  egress {
    protocol   = "-1"
    rule_no    = 100
    action     = "allow"
    cidr_block = "0.0.0.0/0"
    from_port  = 0
    to_port    = 0
  }

  egress {
    protocol        = "-1"
    rule_no         = 200
    action          = "allow"
    ipv6_cidr_block = "::/0"
    from_port       = 0
    to_port         = 0
  }

  tags = {
    Name = "${var.name}-all"
  }
}

# VPC
output "vpc_id" {
  value = module.vpc.vpc_id
}

output "vpc_cidr" {
  value = module.vpc.vpc_cidr
}

output "egress_gateway_id" {
  value = module.vpc.egress_gateway_id
}

# Subnets
output "public_subnet_tier" {
  value = module.public_subnet.tier
}

output "private_subnet_tier" {
  value = module.private_subnet.tier
}

output "build_subnet_ids" {
  value = module.management.build_subnet_ids
}

# NAT
output "nat_gateway_ids" {
  value = module.nat.nat_gateway_ids
}

# VPC Endpoints
output "s3_endpoint_prefix_list_id" {
  value = module.management.s3_endpoint_prefix_list_id
}

output "ssm_security_group_id" {
  value = module.management.ssm_security_group_id
}

