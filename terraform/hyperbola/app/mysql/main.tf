variable "vpc_id" {}
variable "azs" {}
variable "name" {}
variable "env" {}
variable "database_password" {}

data "aws_vpc" "current" {
  id = "${var.vpc_id}"
}

resource "aws_db_instance" "main_rds_instance" {
  identifier_prefix = "app-mysql-"
  allocated_storage = "5"
  engine            = "mysql"
  engine_version    = "5.7"
  instance_class    = "db.t2.micro"

  name     = "hyperbola"
  username = "app"
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

  final_snapshot_identifier = "app-mysql-final-snapshot"
  skip_final_snapshot       = false

  maintenance_window      = "sun:10:18-sun:10:48" # UTC
  backup_retention_period = 10
  backup_window           = "09:22-09:52"         # UTC

  tags {
    Name        = "${var.name}"
    Environment = "${var.env}"
  }
}

resource "aws_db_parameter_group" "main_rds_instance" {
  name_prefix = "app-mysql-custom-params-"
  family      = "mysql5.7"

  parameter {
    name  = "sql_mode"
    value = "traditional"
  }

  parameter {
    name  = "innodb_strict_mode"
    value = "1"
  }

  parameter {
    name  = "character_set_client"
    value = "utf8mb4"
  }

  parameter {
    name  = "character_set_database"
    value = "utf8mb4"
  }

  parameter {
    name  = "character_set_results"
    value = "utf8mb4"
  }

  parameter {
    name  = "character_set_connection"
    value = "utf8mb4"
  }

  parameter {
    name  = "character_set_server"
    value = "utf8mb4"
  }

  parameter {
    name  = "collation_connection"
    value = "utf8mb4_unicode_ci"
  }

  parameter {
    name  = "collation_server"
    value = "utf8mb4_unicode_ci"
  }

  tags {
    Environment = "${var.env}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

module "tier" {
  source = "../../../aws/network/subnet_tier"
}

module "mysql-subnets" {
  source = "../../../aws/network/private_subnet"

  name   = "${var.name}"
  vpc_id = "${data.aws_vpc.current.id}"
  azs    = "${var.azs}"

  subnet_tier       = "${module.tier.private-mysql-rds}"
  nat_enabled       = "false"
  nat_gateway_ids   = ""
  egress_gateway_id = ""
}

resource "aws_db_subnet_group" "main_db_subnet_group" {
  name_prefix = "app-mysql-subnet-group-"
  description = "RDS subnet group"
  subnet_ids  = ["${split(",", module.mysql-subnets.subnet_ids)}"]

  tags {
    Environment = "${var.env}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

# Security groups
resource "aws_security_group" "main_db_access" {
  name_prefix = "app-mysql-sg-"
  description = "Allow access to the database"
  vpc_id      = "${data.aws_vpc.current.id}"

  tags {
    Name        = "${var.name}-sg"
    Environment = "${var.env}"
  }

  lifecycle {
    create_before_destroy = true
  }
}

output "mysql_endpoint" {
  value = "${aws_db_instance.main_rds_instance.address}"
}

output "mysql_port" {
  value = "3306"
}

output "mysql_security_group_id" {
  value = "${aws_security_group.main_db_access.id}"
}
