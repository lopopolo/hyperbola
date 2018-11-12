#--------------------------------------------------------------
# This module creates all resources necessary for a public
# subnet
#--------------------------------------------------------------

variable "name" {}

variable "vpc_id" {}
variable "azs" {}
variable "internet_gateway_id" {}
variable "egress_gateway_id" {}

variable "subnet_tier" {}

data "aws_vpc" "this" {
  id = "${var.vpc_id}"
}

resource "aws_subnet" "public" {
  vpc_id            = "${data.aws_vpc.this.id}"
  cidr_block        = "${cidrsubnet(cidrsubnet(data.aws_vpc.this.cidr_block, 3, var.subnet_tier), 5, count.index)}"
  availability_zone = "${element(split(",", var.azs), count.index)}"
  count             = "${length(split(",", var.azs))}"

  ipv6_cidr_block                 = "${cidrsubnet(cidrsubnet(data.aws_vpc.this.ipv6_cidr_block, 3, var.subnet_tier), 5, count.index)}"
  assign_ipv6_address_on_creation = true

  tags {
    Name    = "${var.name}.${element(split(",", var.azs), count.index)}"
    Network = "subnet-tier-${var.subnet_tier}"
  }

  lifecycle {
    create_before_destroy = true
  }

  map_public_ip_on_launch = true
}

resource "aws_route_table" "public" {
  vpc_id = "${data.aws_vpc.this.id}"

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${var.internet_gateway_id}"
  }

  route {
    ipv6_cidr_block = "::/0"
    gateway_id      = "${var.internet_gateway_id}"
  }

  tags {
    Name = "${var.name}.${element(split(",", var.azs), count.index)}"
  }
}

resource "aws_route_table_association" "public" {
  count          = "${length(split(",", var.azs))}"
  subnet_id      = "${element(aws_subnet.public.*.id, count.index)}"
  route_table_id = "${aws_route_table.public.id}"
}

output "subnet_ids" {
  value = "${aws_subnet.public.*.id}"
}

output "tier" {
  value      = "subnet-tier-${var.subnet_tier}"
  depends_on = ["aws_subnet.public"]
}

output "route_table" {
  value = "${aws_route_table.public.*.id}"
}
