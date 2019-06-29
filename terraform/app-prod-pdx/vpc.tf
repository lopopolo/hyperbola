variable "vpc_cidr" {
  default = "10.149.0.0/16"
}

variable "azs" {
  default = "us-west-2a,us-west-2b,us-west-2c"
}

module "network" {
  source      = "../modules/aws/network"
  name        = var.name
  vpc_cidr    = var.vpc_cidr
  azs         = var.azs
  nat_enabled = "false"
  region      = var.region
}
