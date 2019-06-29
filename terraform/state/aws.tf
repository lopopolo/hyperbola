variable "region" {
  default = "us-east-1"
}

provider "aws" {
  region  = "${var.region}"
  version = "~> 2.17.0"
}
