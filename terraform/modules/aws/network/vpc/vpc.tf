#--------------------------------------------------------------
# This module creates all resources necessary for a VPC
#--------------------------------------------------------------

variable "name" {}
variable "cidr" {}

resource "aws_vpc" "this" {
  cidr_block           = "${var.cidr}"
  enable_dns_support   = true
  enable_dns_hostnames = true

  assign_generated_ipv6_cidr_block = true

  tags = {
    Name = "${var.name}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_internet_gateway" "this" {
  vpc_id = "${aws_vpc.this.id}"

  tags = {
    Name = "${var.name}"
  }
}

resource "aws_egress_only_internet_gateway" "this" {
  vpc_id = "${aws_vpc.this.id}"
}

output "vpc_id" {
  value = "${aws_vpc.this.id}"
}

output "vpc_cidr" {
  value = "${aws_vpc.this.cidr_block}"
}

output "vpc_cidr_ipv6" {
  value = "${aws_vpc.this.ipv6_cidr_block}"
}

output "internet_gateway_id" {
  value = "${aws_internet_gateway.this.id}"
}

output "egress_gateway_id" {
  value = "${aws_egress_only_internet_gateway.this.id}"
}
