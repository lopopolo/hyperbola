terraform {
  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/lab/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

variable "name" {
  default = "lab"
}

variable "env" {
  default = "stage"
}

variable "vpc_cidr" {
  default = "10.111.0.0/16"
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

