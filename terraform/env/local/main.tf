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

resource "aws_route53_record" "wiki-local" {
  zone_id = "${data.aws_route53_zone.local-dc.zone_id}"
  name    = "wiki"
  type    = "A"

  ttl     = 300
  records = ["192.168.10.10"]
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

resource "aws_route53_record" "redis-CNAME" {
  zone_id = "${data.aws_route53_zone.local-dc.id}"
  name    = "redis"
  type    = "CNAME"
  ttl     = 300

  records = ["app.local.hyperboladc.net"]
}
