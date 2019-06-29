variable "region" {
  default = "us-west-2"
}

provider "aws" {
  region  = "${var.region}"
  version = "~> 2.17.0"
}
