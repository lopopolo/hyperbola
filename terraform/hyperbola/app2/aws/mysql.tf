variable "database_password" {}

resource "aws_db_instance" "main_rds_instance" {
  identifier        = "${var.env}-mysql"
  allocated_storage = "5"
  engine            = "mysql"
  engine_version    = "5.7"
  instance_class    = "db.t2.micro"

  name     = "hyperbola${var.env}"
  username = "${var.env}user"
  password = "${var.database_password}"
  port     = "3306"

  vpc_security_group_ids = ["${aws_security_group.main_db_access.id}"]
  db_subnet_group_name   = "${aws_db_subnet_group.main_db_subnet_group.name}"
  parameter_group_name   = "${aws_db_parameter_group.main_rds_instance.id}"

  multi_az            = true
  storage_type        = "gp2"
  publicly_accessible = false

  allow_major_version_upgrade = false
  auto_minor_version_upgrade  = true

  tags {
    Environment = "${var.env}"
  }
}

resource "aws_db_parameter_group" "main_rds_instance" {
  name   = "${var.env}-mysql-custom-params"
  family = "mysql5.7"

  parameter {
    name  = "sql_mode"
    value = "TRADITIONAL"
  }

  parameter {
    name  = "character_set_server"
    value = "utf8mb4"
  }

  parameter {
    name  = "character_set_client"
    value = "utf8mb4"
  }

  parameter {
    name  = "collation_server"
    value = "utf8mb4_unicode_ci"
  }

  tags {
    Environment = "${var.env}"
  }
}

module "mysql-subnets" {
  source = "../../../aws/network/private_subnet"

  name   = "${var.name}-private-mysql"
  vpc_id = "${data.aws_vpc.current.id}"
  azs    = "${var.azs}"

  subnet_tier       = "${module.tier.private-mysql}"
  nat_enabled       = false
  nat_gateway_ids   = ""
  egress_gateway_id = ""
}

resource "aws_db_subnet_group" "main_db_subnet_group" {
  name        = "${var.env}-mysql-subnetgrp"
  description = "RDS subnet group"
  subnet_ids  = ["${split(",", module.mysql-subnets.subnet_ids)}"]

  tags {
    Environment = "${var.env}"
  }
}

# Security groups
resource "aws_security_group" "main_db_access" {
  name_prefix = "${var.env}-mysql-sg"
  description = "Allow access to the database"
  vpc_id      = "${data.aws_vpc.current.id}"

  tags {
    Environment = "${var.env}"
  }
}

output "mysql_endpoint" {
  value = "${aws_db_instance.main_rds_instance.address}"
}

output "mysql_port" {
  value = "3306"
}
