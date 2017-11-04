variable "bastion_security_group_id" {}
variable "s3_endpoint_prefix_list_id" {}

variable "mysql_port" {}
variable "mysql_security_group_id" {}

resource "aws_security_group" "backend" {
  name_prefix = "app-backend-sg-"
  vpc_id      = "${var.vpc_id}"

  tags {
    Name        = "${var.name}-backend-sg"
    Environment = "${var.env}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_security_group_rule" "backend-from-bastion-ssh" {
  type                     = "ingress"
  protocol                 = "tcp"
  from_port                = 22
  to_port                  = 22
  security_group_id        = "${aws_security_group.backend.id}"
  source_security_group_id = "${var.bastion_security_group_id}"
}

resource "aws_security_group_rule" "backend-from-alb-http" {
  type                     = "ingress"
  protocol                 = "tcp"
  from_port                = 80
  to_port                  = 80
  security_group_id        = "${aws_security_group.backend.id}"
  source_security_group_id = "${aws_security_group.alb.id}"
}

resource "aws_security_group_rule" "backend-from-alb-health-check" {
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

resource "aws_security_group_rule" "backend-to-s3-endpoint" {
  type              = "egress"
  protocol          = "-1"
  from_port         = 0
  to_port           = 0
  security_group_id = "${aws_security_group.backend.id}"
  prefix_list_ids   = ["${var.s3_endpoint_prefix_list_id}"]
}

output "backend_security_group_id" {
  value = "${aws_security_group.backend.id}"
}
