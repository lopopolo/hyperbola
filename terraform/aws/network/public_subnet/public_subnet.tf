#--------------------------------------------------------------
# This module creates all resources necessary for a public
# subnet
#--------------------------------------------------------------

variable "name" {
  default = "public"
}

variable "vpc_id" {}
variable "cidrs" {}
variable "azs" {}
variable "egress_gateway_id" {}

data "aws_vpc" "current" {
  id = "${var.vpc_id}"
}

resource "aws_internet_gateway" "public" {
  vpc_id = "${data.aws_vpc.current.id}"

  tags {
    Name = "${var.name}"
  }
}

resource "aws_subnet" "public" {
  vpc_id            = "${data.aws_vpc.current.id}"
  cidr_block        = "${element(split(",", var.cidrs), count.index)}"
  availability_zone = "${element(split(",", var.azs), count.index)}"
  count             = "${length(split(",", var.cidrs))}"

  ipv6_cidr_block                 = "${cidrsubnet(data.aws_vpc.current.ipv6_cidr_block, 8 ,10 + count.index)}"
  assign_ipv6_address_on_creation = true

  tags {
    Name    = "${var.name}.${element(split(",", var.azs), count.index)}"
    Network = "${var.name}"
  }

  lifecycle {
    create_before_destroy = true
  }

  map_public_ip_on_launch = true
}

resource "aws_route_table" "public" {
  vpc_id = "${data.aws_vpc.current.id}"

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.public.id}"
  }

  route {
    ipv6_cidr_block = "::/0"
    gateway_id      = "${aws_internet_gateway.public.id}"
  }

  tags {
    Name = "${var.name}.${element(split(",", var.azs), count.index)}"
  }
}

resource "aws_route_table_association" "public" {
  count          = "${length(split(",", var.cidrs))}"
  subnet_id      = "${element(aws_subnet.public.*.id, count.index)}"
  route_table_id = "${aws_route_table.public.id}"
}

output "subnet_ids" {
  value = "${join(",", aws_subnet.public.*.id)}"
}

output "tag_value" {
  value      = "${var.name}"
  depends_on = ["aws_subnet.public"]
}
