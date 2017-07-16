#--------------------------------------------------------------
# This module creates all resources necessary for a VPC
#--------------------------------------------------------------

variable "name" {
  default = "vpc"
}

variable "cidr" {}

resource "aws_vpc" "vpc" {
  cidr_block           = "${var.cidr}"
  enable_dns_support   = true
  enable_dns_hostnames = true

  assign_generated_ipv6_cidr_block = true

  tags {
    Name = "${var.name}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_egress_only_internet_gateway" "vpc" {
  vpc_id = "${aws_vpc.vpc.id}"
}

output "vpc_id" {
  value = "${aws_vpc.vpc.id}"
}

output "vpc_cidr" {
  value = "${aws_vpc.vpc.cidr_block}"
}

output "vpc_cidr_ipv6" {
  value = "${aws_vpc.vpc.ipv6_cidr_block}"
}

output "egress_gateway_id" {
  value = "${aws_egress_only_internet_gateway.vpc.id}"
}
