data "aws_route53_zone" "dc" {
  name         = "hyperboladc.net."
  private_zone = false
}

data "aws_route53_zone" "aws-dc" {
  name         = "aws.hyperboladc.net."
  private_zone = false
}

data "aws_route53_zone" "hyperbola-zone" {
  name         = "hyperbo.la."
  private_zone = false
}

resource "aws_route53_record" "mysql-prod" {
  zone_id = "${data.aws_route53_zone.dc.id}"
  name    = "mysql-prod"
  type    = "CNAME"
  ttl     = 300

  records = ["${module.hyperbola-app-mysql2.mysql_endpoint}"]
}

resource "aws_route53_record" "bastion-prod" {
  zone_id = "${data.aws_route53_zone.dc.id}"
  name    = "bastion-prod"
  type    = "A"
  ttl     = 300

  records = ["${module.network.bastion_public_ip}"]
}

resource "aws_route53_record" "mysql2-CNAME" {
  zone_id = "${data.aws_route53_zone.aws-dc.id}"
  name    = "mysql2"
  type    = "CNAME"
  ttl     = 300

  records = ["${module.hyperbola-app-mysql2.mysql_endpoint}"]
}

resource "aws_route53_record" "bastion-A" {
  zone_id = "${data.aws_route53_zone.aws-dc.id}"
  name    = "app-bastion"
  type    = "A"
  ttl     = 300

  records = ["${module.network.bastion_public_ip}"]
}

variable "cloudflare_email" {
  default = "rjl@hyperbo.la"
}

variable "cloudflare_token" {}

provider "cloudflare" {
  email = "${var.cloudflare_email}"
  token = "${var.cloudflare_token}"
}

resource "cloudflare_record" "hyperbo_la" {
  domain  = "hyperbo.la"
  name    = "hyperbo.la"
  value   = "${module.hyperbola-app-backend.alb_dns}"
  type    = "CNAME"
  ttl     = 1
  proxied = false
}

resource "cloudflare_record" "www_hyperbo_la" {
  domain  = "hyperbo.la"
  name    = "www"
  value   = "${module.hyperbola-app-backend.alb_dns}"
  type    = "CNAME"
  ttl     = 1
  proxied = false
}

resource "aws_route53_record" "hyperbo_la_A" {
  zone_id = "${data.aws_route53_zone.hyperbola-zone.zone_id}"
  name    = "hyperbo.la"
  type    = "A"

  alias {
    name                   = "${module.hyperbola-app-backend.alb_dns}"
    zone_id                = "${module.hyperbola-app-backend.alb_zone_id}"
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "hyperbo_la_AAAA" {
  zone_id = "${data.aws_route53_zone.hyperbola-zone.zone_id}"
  name    = "hyperbo.la"
  type    = "AAAA"

  alias {
    name                   = "${module.hyperbola-app-backend.alb_dns}"
    zone_id                = "${module.hyperbola-app-backend.alb_zone_id}"
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "www_hyperbo_la_A" {
  zone_id = "${data.aws_route53_zone.hyperbola-zone.zone_id}"
  name    = "www"
  type    = "A"

  alias {
    name                   = "${module.hyperbola-app-backend.alb_dns}"
    zone_id                = "${module.hyperbola-app-backend.alb_zone_id}"
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "www_hyperbo_la_AAAA" {
  zone_id = "${data.aws_route53_zone.hyperbola-zone.zone_id}"
  name    = "www"
  type    = "AAAA"

  alias {
    name                   = "${module.hyperbola-app-backend.alb_dns}"
    zone_id                = "${module.hyperbola-app-backend.alb_zone_id}"
    evaluate_target_health = true
  }
}
