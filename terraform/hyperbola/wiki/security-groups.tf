variable "github_cidrs" {
  type    = "list"
  default = ["192.30.252.0/22", "185.199.108.0/22"]
}

variable "github_ipv6_cidrs" {
  type    = "list"
  default = ["2620:112:3000::/44"]
}

variable "github_ports" {
  type    = "list"
  default = [22, 80, 443, 9418]
}

variable "bastion_security_group_id" {}

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

# github: https://help.github.com/articles/what-ip-addresses-does-github-use-that-i-should-whitelist/
resource "aws_security_group_rule" "backend-to-github" {
  count             = "${length(var.github_ports)}"
  type              = "egress"
  protocol          = "tcp"
  from_port         = "${element(var.github_ports, count.index)}"
  to_port           = "${element(var.github_ports, count.index)}"
  cidr_blocks       = ["${var.github_cidrs}"]
  ipv6_cidr_blocks  = ["${var.github_ipv6_cidrs}"]
  security_group_id = "${aws_security_group.backend.id}"
}

resource "aws_security_group_rule" "elb-to-backend-80" {
  type                     = "ingress"
  protocol                 = "tcp"
  from_port                = 80
  to_port                  = 80
  security_group_id        = "${aws_security_group.backend.id}"
  source_security_group_id = "${aws_security_group.alb.id}"
}

resource "aws_security_group_rule" "elb-to-backend-8888" {
  type                     = "ingress"
  protocol                 = "tcp"
  from_port                = 8888
  to_port                  = 8888
  security_group_id        = "${aws_security_group.backend.id}"
  source_security_group_id = "${aws_security_group.alb.id}"
}
