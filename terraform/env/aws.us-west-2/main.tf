variable "name" {
  default = "hyperbola-production-us-west-2"
}

variable "hyperbola_app_rds_password" {}

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

resource "aws_route53_record" "redis-CNAME" {
  zone_id = "${data.aws_route53_zone.aws-dc.id}"
  name    = "redis"
  type    = "CNAME"
  ttl     = 300

  records = ["${module.hyperbola-app-aws.redis_endpoint}"]
}

resource "aws_route53_record" "mysql-CNAME" {
  zone_id = "${data.aws_route53_zone.aws-dc.id}"
  name    = "mysql"
  type    = "CNAME"
  ttl     = 300

  records = ["${module.hyperbola-app-aws.mysql_endpoint}"]
}

module "hyperbola-app-aws" {
  source = "../../hyperbola/app2/aws"
  name   = "${var.name}"
  env    = "production"

  vpc_id = "${module.network.vpc_id}"
  azs    = "${var.azs}"

  database_password = "${var.hyperbola_app_rds_password}"
}

module "hyperbola-app-base" {
  source = "../../hyperbola/app2/base"
  env    = "production"
  bucket = "www"
}

output "redis_endpoint" {
  value = "${module.hyperbola-app-aws.redis_endpoint}"
}

output "mysql_endpoint" {
  value = "${module.hyperbola-app-aws.mysql_endpoint}"
}

output "backup_bucket" {
  value = "${module.hyperbola-app-base.backup_bucket}"
}

output "media_bucket" {
  value = "${module.hyperbola-app-base.media_bucket}"
}
