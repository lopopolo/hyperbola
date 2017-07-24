data "aws_route53_zone" "aws-dc" {
  name         = "aws.hyperboladc.net."
  private_zone = false
}

resource "aws_route53_record" "redis-CNAME" {
  zone_id = "${data.aws_route53_zone.aws-dc.id}"
  name    = "redis"
  type    = "CNAME"
  ttl     = 300

  records = ["${module.hyperbola-app-redis.redis_endpoint}"]
}

resource "aws_route53_record" "mysql-CNAME" {
  zone_id = "${data.aws_route53_zone.aws-dc.id}"
  name    = "mysql"
  type    = "CNAME"
  ttl     = 300

  records = ["${module.hyperbola-app-mysql.mysql_endpoint}"]
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
