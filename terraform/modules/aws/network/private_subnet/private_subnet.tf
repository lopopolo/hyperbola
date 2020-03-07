#--------------------------------------------------------------
# This module creates all resources necessary for a private
# subnet
#--------------------------------------------------------------

variable "name" {}

variable "vpc_id" {}
variable "azs" {}

variable "nat_enabled" {
  # https://www.terraform.io/docs/configuration/variables.html#booleans
  type    = "string"
  default = "true"
}

variable "nat_gateway_ids" {}
variable "egress_gateway_id" {}

variable "subnet_tier" {}

data "aws_vpc" "this" {
  id = "${var.vpc_id}"
}

resource "aws_subnet" "private" {
  vpc_id            = "${data.aws_vpc.this.id}"
  cidr_block        = "${cidrsubnet(cidrsubnet(data.aws_vpc.this.cidr_block, 3, var.subnet_tier), 5, count.index)}"
  availability_zone = "${element(split(",", var.azs), count.index)}"
  count             = "${length(split(",", var.azs))}"

  ipv6_cidr_block                 = "${cidrsubnet(cidrsubnet(data.aws_vpc.this.ipv6_cidr_block, 3, var.subnet_tier), 5, count.index)}"
  assign_ipv6_address_on_creation = true

  tags = {
    Name    = "${var.name}.${element(split(",", var.azs), count.index)}"
    Network = "subnet-tier-${var.subnet_tier}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route_table" "private" {
  vpc_id = "${data.aws_vpc.this.id}"
  count  = "${length(split(",", var.azs))}"

  tags = {
    Name = "${var.name}.${element(split(",", var.azs), count.index)}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route" "nat_gateway" {
  count = "${var.nat_enabled == "true" ? length(split(",", var.azs)) : 0}"

  route_table_id         = aws_route_table.private[count.index].id
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id         = "${element(split(",", var.nat_gateway_ids), count.index)}"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route" "ipv6_egress_gateway" {
  count = "${var.nat_enabled == "true" ? length(split(",", var.azs)) : 0}"

  route_table_id         = aws_route_table.private[count.index].id
  destination_cidr_block = "::/0"
  egress_only_gateway_id = "${var.egress_gateway_id}"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route_table_association" "private" {
  count          = "${length(split(",", var.azs))}"
  subnet_id      = aws_subnet.private[count.index].id
  route_table_id = aws_route_table.private[count.index].id

  lifecycle {
    create_before_destroy = true
  }
}

output "subnet_ids" {
  value = "${aws_subnet.private.*.id}"
}

output "tier" {
  value      = "subnet-tier-${var.subnet_tier}"
  depends_on = [aws_subnet.private]
}

output "route_table" {
  value = "${aws_route_table.private.*.id}"
}
