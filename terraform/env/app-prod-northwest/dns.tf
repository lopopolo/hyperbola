data "aws_route53_zone" "dc" {
  name         = "hyperboladc.net."
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

  records = ["${module.hyperbola-app-mysql.mysql_endpoint}"]
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
