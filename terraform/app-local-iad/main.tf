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

variable "env" {
  default = "local"
}

variable "app_secret_key" {}

variable "app_database_password" {}

data "aws_route53_zone" "dc" {
  name         = "hyperboladc.net."
  private_zone = false
}

resource "aws_route53_record" "app-local" {
  zone_id = "${data.aws_route53_zone.dc.zone_id}"
  name    = "app-local"
  type    = "A"
  ttl     = "300"
  records = ["192.168.10.20"]
}

resource "aws_route53_record" "lb-local" {
  zone_id = "${data.aws_route53_zone.dc.zone_id}"
  name    = "lb-local"
  type    = "A"
  ttl     = "300"
  records = ["192.168.10.40"]
}

resource "aws_route53_record" "local" {
  zone_id = "${data.aws_route53_zone.dc.zone_id}"
  name    = "local"
  type    = "CNAME"
  ttl     = "300"
  records = ["${aws_route53_record.lb-local.fqdn}"]
}

module "base" {
  source = "../modules/hyperbola/app/base"
  env    = "${var.env}"
  bucket = "local"
}

module "secrets" {
  source = "../modules/hyperbola/app/secrets"
  env    = "${var.env}"

  secret_key        = "${var.app_secret_key}"
  database_password = "${var.app_database_password}"
}

module "iam_r53" {
  source = "../modules/aws/util/iam"

  name  = "local-route53"
  users = "local-lb"

  policy = <<EOF
{
  "Version"  : "2012-10-17",
  "Statement": [
    {
      "Sid" : "AllowRecordSetsPermissions",
      "Effect": "Allow",
      "Action": [
        "route53:GetHostedZone",
        "route53:ListHostedZones",
        "route53:ChangeResourceRecordSets",
        "route53:ListResourceRecordSets",
        "route53:GetChange",
        "route53:GetHostedZoneCount",
        "route53:ListHostedZonesByName"
      ],
      "Resource": [
        "arn:aws:route53:::hostedzone/${data.aws_route53_zone.dc.id}"
      ]
    }
  ]
}
EOF
}

module "iam_vagrant" {
  source = "../modules/aws/util/iam"

  name  = "local-app-s3"
  users = "local-app"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid" : "AllowMediaBucketPermissions",
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": [
        "${module.base.media_bucket_arn}",
        "${module.base.media_bucket_arn}/*",
        "${module.base.backup_bucket_arn}",
        "${module.base.backup_bucket_arn}/*"
      ]
    },
    {
      "Sid" : "AllowSecretsAccess",
      "Effect": "Allow",
      "Action": [
        "ssm:GetParameter",
        "ssm:GetParameters",
        "ssm:GetParametersByPath"
      ],
      "Resource": [
        "arn:aws:ssm:*:*:parameter/app/${var.env}",
        "arn:aws:ssm:*:*:parameter/app/${var.env}/",
        "arn:aws:ssm:*:*:parameter/app/${var.env}/*"
      ]
    }
  ]
}
EOF
}

output "config" {
  value = <<CONFIG

Route53 IAM:
  Route53 Users: ${join("\n               ", formatlist("%s", split(",", module.iam_r53.users)))}

  Access IDs: ${join("\n              ", formatlist("%s", split(",", module.iam_r53.access_ids)))}

  Secret Keys: ${join("\n               ", formatlist("%s", split(",", module.iam_r53.secret_keys)))}

Vagrant S3 IAM:
  Vagrant S3 Users: ${join("\n               ", formatlist("%s", split(",", module.iam_vagrant.users)))}

  Access IDs: ${join("\n              ", formatlist("%s", split(",", module.iam_vagrant.access_ids)))}

  Secret Keys: ${join("\n               ", formatlist("%s", split(",", module.iam_vagrant.secret_keys)))}

CONFIG
}
