#--------------------------------------------------------------
# This module creates all resources necessary for a private
# subnet
#--------------------------------------------------------------

variable "name" {
  default = "private"
}

variable "vpc_id" {}
variable "azs" {}

variable "nat_enabled" {
  default = true
}

variable "nat_gateway_ids" {}
variable "egress_gateway_id" {}

variable "subnet_tier" {}

data "aws_vpc" "current" {
  id = "${var.vpc_id}"
}

resource "aws_subnet" "private" {
  vpc_id            = "${data.aws_vpc.current.id}"
  cidr_block        = "${cidrsubnet(cidrsubnet(data.aws_vpc.current.cidr_block, 3, var.subnet_tier), 5, count.index)}"
  availability_zone = "${element(split(",", var.azs), count.index)}"
  count             = "${length(split(",", var.azs))}"

  ipv6_cidr_block                 = "${cidrsubnet(cidrsubnet(data.aws_vpc.current.ipv6_cidr_block, 3, var.subnet_tier), 5, count.index)}"
  assign_ipv6_address_on_creation = true

  tags {
    Name    = "${var.name}.${element(split(",", var.azs), count.index)}"
    Network = "subnet-tier-${var.subnet_tier}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route_table" "private" {
  vpc_id = "${data.aws_vpc.current.id}"
  count  = "${var.nat_enabled ? length(split(",", var.azs)) : 0}"

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = "${element(split(",", var.nat_gateway_ids), count.index)}"
  }

  route {
    ipv6_cidr_block        = "::/0"
    egress_only_gateway_id = "${var.egress_gateway_id}"
  }

  tags {
    Name = "${var.name}.${element(split(",", var.azs), count.index)}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route_table_association" "private" {
  count          = "${var.nat_enabled ? length(split(",", var.azs)) : 0}"
  subnet_id      = "${element(aws_subnet.private.*.id, count.index)}"
  route_table_id = "${element(aws_route_table.private.*.id, count.index)}"

  lifecycle {
    create_before_destroy = true
  }
}

output "subnet_ids" {
  value = "${join(",", aws_subnet.private.*.id)}"
}

output "tier" {
  value      = "subnet-tier-${var.subnet_tier}"
  depends_on = ["aws_subnet.private.*.id"]
}
