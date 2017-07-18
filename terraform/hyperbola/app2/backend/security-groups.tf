variable "bastion_security_group_id" {}

variable "mysql_port" {}
variable "mysql_security_group_id" {}
variable "redis_port" {}
variable "redis_security_group_id" {}

resource "aws_security_group" "backend" {
  name_prefix = "${var.name}-backend-sg-"
  vpc_id      = "${var.vpc_id}"

  tags {
    Name = "${var.name}-backend"
  }

  lifecycle {
    create_before_destroy = true
  }
}

# ssh from bastion
resource "aws_security_group_rule" "ssh-to-backend" {
  type                     = "ingress"
  protocol                 = "tcp"
  from_port                = 22
  to_port                  = 22
  security_group_id        = "${aws_security_group.backend.id}"
  source_security_group_id = "${var.bastion_security_group_id}"
}

resource "aws_security_group_rule" "alb-to-backend-80" {
  type                     = "ingress"
  protocol                 = "tcp"
  from_port                = 80
  to_port                  = 80
  security_group_id        = "${aws_security_group.backend.id}"
  source_security_group_id = "${aws_security_group.alb.id}"
}

resource "aws_security_group_rule" "alb-to-backend-8888" {
  type                     = "ingress"
  protocol                 = "tcp"
  from_port                = 8888
  to_port                  = 8888
  security_group_id        = "${aws_security_group.backend.id}"
  source_security_group_id = "${aws_security_group.alb.id}"
}

resource "aws_security_group_rule" "backend-to-mysql" {
  type                     = "egress"
  protocol                 = "tcp"
  from_port                = "${var.mysql_port}"
  to_port                  = "${var.mysql_port}"
  security_group_id        = "${aws_security_group.backend.id}"
  source_security_group_id = "${var.mysql_security_group_id}"
}

resource "aws_security_group_rule" "mysql-from-backend" {
  type                     = "ingress"
  protocol                 = "tcp"
  from_port                = "${var.mysql_port}"
  to_port                  = "${var.mysql_port}"
  security_group_id        = "${var.mysql_security_group_id}"
  source_security_group_id = "${aws_security_group.backend.id}"
}

resource "aws_security_group_rule" "backend-to-redis" {
  type                     = "egress"
  protocol                 = "tcp"
  from_port                = "${var.redis_port}"
  to_port                  = "${var.redis_port}"
  security_group_id        = "${aws_security_group.backend.id}"
  source_security_group_id = "${var.redis_security_group_id}"
}

resource "aws_security_group_rule" "redis-from-backend" {
  type                     = "ingress"
  protocol                 = "tcp"
  from_port                = "${var.redis_port}"
  to_port                  = "${var.redis_port}"
  security_group_id        = "${var.redis_security_group_id}"
  source_security_group_id = "${aws_security_group.backend.id}"
}

output "backend_security_group_id" {
  value = "${aws_security_group.backend.id}"
}
