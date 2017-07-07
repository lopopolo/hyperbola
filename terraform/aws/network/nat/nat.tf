#--------------------------------------------------------------
# This module creates all resources necessary for NAT
#--------------------------------------------------------------

variable "name" {
  default = "nat"
}

variable "vpc_id" {}
variable "public_subnet_name" {}

data "aws_vpc" "selected" {
  id = "${var.vpc_id}"
}

data "aws_subnet_ids" "public" {
  vpc_id = "${data.aws_vpc.selected.id}"

  tags {
    Network = "${var.public_subnet_name}"
  }
}

resource "aws_eip" "nat" {
  vpc = true

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_nat_gateway" "nat" {
  allocation_id = "${element(aws_eip.nat.*.id, count.index)}"
  subnet_id     = "${data.aws_subnet_ids.public.ids[count.index]}"

  # count = "${length(split(",", var.azs))}" # Comment out count to only have 1 NAT

  lifecycle {
    create_before_destroy = true
  }
}

output "nat_gateway_ids" {
  value = "${join(",", aws_nat_gateway.nat.*.id)}"
}
