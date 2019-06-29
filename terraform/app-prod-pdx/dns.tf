resource "aws_route53_zone" "app_dc" {
  name = "app.hyperboladc.net"

  vpc {
    vpc_id = module.network.vpc_id
  }
}

data "aws_route53_zone" "hyperbola" {
  name         = "hyperbo.la."
  private_zone = false
}

resource "aws_route53_record" "mysql" {
  zone_id = aws_route53_zone.app_dc.id
  name    = "mysql"
  type    = "CNAME"
  ttl     = 300

  records = [module.mysql.endpoint]
}

resource "aws_route53_record" "hyperbo_la_A" {
  zone_id = data.aws_route53_zone.hyperbola.zone_id
  name    = "hyperbo.la"
  type    = "A"

  alias {
    name                   = module.backend.alb_dns
    zone_id                = module.backend.alb_zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "hyperbo_la_AAAA" {
  zone_id = data.aws_route53_zone.hyperbola.zone_id
  name    = "hyperbo.la"
  type    = "AAAA"

  alias {
    name                   = module.backend.alb_dns
    zone_id                = module.backend.alb_zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "www_hyperbo_la_A" {
  zone_id = data.aws_route53_zone.hyperbola.zone_id
  name    = "www"
  type    = "A"

  alias {
    name                   = module.backend.alb_dns
    zone_id                = module.backend.alb_zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "www_hyperbo_la_AAAA" {
  zone_id = data.aws_route53_zone.hyperbola.zone_id
  name    = "www"
  type    = "AAAA"

  alias {
    name                   = module.backend.alb_dns
    zone_id                = module.backend.alb_zone_id
    evaluate_target_health = true
  }
}
