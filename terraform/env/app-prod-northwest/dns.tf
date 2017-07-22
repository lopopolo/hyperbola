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
