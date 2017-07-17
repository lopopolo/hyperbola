variable "name" {}
variable "env" {}

variable "vpc_id" {}
variable "azs" {}

data "aws_vpc" "current" {
  id = "${var.vpc_id}"
}

module "tier" {
  source = "../../../aws/network/subnet_tier"
}
