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

module "hyperbola-app-aws" {
  source = "../../hyperbola/app/base"
  env    = "local"
  bucket = "local"
}

module "iam_r53" {
  source = "../../aws/util/iam"

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
      "Resource": "*"
    }
  ]
}
EOF
}

module "iam_vagrant" {
  source = "../../aws/util/iam"

  name  = "local-app-s3"
  users = "local-app"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement":[{
    "Effect": "Allow",
    "Action": "s3:*",
    "Resource": ["${module.hyperbola-app-aws.media_bucket_arn}",
                 "${module.hyperbola-app-aws.media_bucket_arn}/*",
                 "${module.hyperbola-app-aws.backup_bucket_arn}",
                 "${module.hyperbola-app-aws.backup_bucket_arn}/*"]
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
