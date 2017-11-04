terraform {
  required_version = "> 0.9.7"

  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/hyperbola-local/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

data "aws_route53_zone" "local-dc" {
  name         = "local.hyperboladc.net."
  private_zone = false
}

resource "aws_route53_record" "app-local-dc" {
  zone_id = "${data.aws_route53_zone.local-dc.zone_id}"
  name    = "app"
  type    = "A"
  ttl     = "300"
  records = ["192.168.10.20"]
}

module "hyperbola-app-aws" {
  source = "../../hyperbola/app/base"
  env    = "local"
  bucket = "local"
}
