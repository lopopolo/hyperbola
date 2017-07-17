resource "aws_security_group_rule" "backend-to-mysql" {
  type                     = "egress"
  protocol                 = "tcp"
  from_port                = "${module.hyperbola-app-aws.mysql_port}"
  to_port                  = "${module.hyperbola-app-aws.mysql_port}"
  security_group_id        = "${module.hyperbola-app-backend.backend_security_group_id}"
  source_security_group_id = "${module.hyperbola-app-aws.mysql_security_group_id}"
}

resource "aws_security_group_rule" "mysql-from-backend" {
  type                     = "ingress"
  protocol                 = "tcp"
  from_port                = "${module.hyperbola-app-aws.mysql_port}"
  to_port                  = "${module.hyperbola-app-aws.mysql_port}"
  security_group_id        = "${module.hyperbola-app-aws.mysql_security_group_id}"
  source_security_group_id = "${module.hyperbola-app-backend.backend_security_group_id}"
}

resource "aws_security_group_rule" "backend-to-redis" {
  type                     = "egress"
  protocol                 = "tcp"
  from_port                = "${module.hyperbola-app-aws.redis_port}"
  to_port                  = "${module.hyperbola-app-aws.redis_port}"
  security_group_id        = "${module.hyperbola-app-backend.backend_security_group_id}"
  source_security_group_id = "${module.hyperbola-app-aws.redis_security_group_id}"
}

resource "aws_security_group_rule" "redis-from-backend" {
  type                     = "ingress"
  protocol                 = "tcp"
  from_port                = "${module.hyperbola-app-aws.redis_port}"
  to_port                  = "${module.hyperbola-app-aws.redis_port}"
  security_group_id        = "${module.hyperbola-app-aws.redis_security_group_id}"
  source_security_group_id = "${module.hyperbola-app-backend.backend_security_group_id}"
}
