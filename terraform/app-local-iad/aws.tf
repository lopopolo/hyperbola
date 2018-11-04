variable "region" {
  default = "us-east-1"
}

provider "aws" {
  region  = "${var.region}"
  version = "~> 1.42"
}
