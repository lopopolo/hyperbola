variable "name" {}

terraform {
  required_version = "> 0.9.7"

  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/hyperbola-aws.us-west-2/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

data "aws_route53_zone" "aws-dc" {
  name         = "aws.hyperboladc.net."
  private_zone = false
}

module "hyperbola-app-aws" {
  source = "../../hyperbola/app2/aws"
  name   = "${var.name}"
  env    = "production"

  vpc_id = "${module.network.vpc_id}"
  azs    = "${var.azs}"
}

module "hyperbola-app-base" {
  source              = "../../hyperbola/app2/base"
  env                 = "production"
  bucket              = "www"
  redis               = "${module.hyperbola-app-aws.redis_domain}"
  hyperboladc_zone_id = "${data.aws_route53_zone.aws-dc.zone_id}"
}
