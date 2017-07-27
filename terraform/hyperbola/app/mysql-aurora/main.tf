variable "vpc_id" {}
variable "azs" {}
variable "name" {}
variable "env" {}
variable "database_password" {}

data "aws_vpc" "current" {
  id = "${var.vpc_id}"
}

resource "aws_security_group" "mysql" {
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

module "tier" {
  source = "../../../aws/network/subnet_tier"
}

module "mysql-subnets" {
  source = "../../../aws/network/private_subnet"

  name   = "${var.name}"
  vpc_id = "${data.aws_vpc.current.id}"
  azs    = "${var.azs}"

  subnet_tier       = "${module.tier.private-mysql}"
  nat_enabled       = "false"
  nat_gateway_ids   = ""
  egress_gateway_id = ""
}

resource "aws_db_subnet_group" "mysql" {
  name_prefix = "app-mysql-subnet-group-"
  description = "Aurora subnet group"
  subnet_ids  = ["${split(",", module.mysql-subnets.subnet_ids)}"]

  tags {
    Environment = "${var.env}"
  }
}

resource "aws_rds_cluster" "mysql" {
  cluster_identifier_prefix = "app-mysql-cluster-"
  port                      = "3306"
  database_name             = "app"
  master_username           = "app"
  master_password           = "${var.database_password}"

  vpc_security_group_ids          = ["${aws_security_group.mysql.id}"]
  db_subnet_group_name            = "${aws_db_subnet_group.mysql.name}"
  db_cluster_parameter_group_name = "${aws_rds_cluster_parameter_group.mysql.name}"

  final_snapshot_identifier    = "app-mysql-cluster-final-snapshot"
  skip_final_snapshot          = false
  backup_retention_period      = 30
  preferred_backup_window      = "09:22-09:52"                      # UTC
  preferred_maintenance_window = "sun:10:18-sun:10:48"              # UTC
}

resource "aws_rds_cluster_instance" "mysql" {
  count               = 2
  identifier_prefix   = "app-mysql-cluster-instance-${count.index}-"
  cluster_identifier  = "${aws_rds_cluster.mysql.id}"
  instance_class      = "db.t2.small"
  publicly_accessible = false

  db_subnet_group_name    = "${aws_db_subnet_group.mysql.name}"
  db_parameter_group_name = "${aws_db_parameter_group.mysql.name}"

  tags {
    Name        = "${var.name}-cluster-instance-${count.index}"
    Environment = "${var.env}"
  }
}

resource "aws_db_parameter_group" "mysql" {
  name_prefix = "app-mysql-params-"
  family      = "aurora5.6"

  parameter {
    name  = "sql_mode"
    value = "traditional"
  }

  tags {
    Environment = "${var.env}"
  }
}

resource "aws_rds_cluster_parameter_group" "mysql" {
  name_prefix = "app-mysql-cluster-params-"
  family      = "aurora5.6"

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
}

output "mysql_endpoint" {
  value = "${aws_rds_cluster.mysql.endpoint}"
}

output "mysql_read_only_endpoint" {
  value = "${aws_rds_cluster.mysql.reader_endpoint}"
}

output "mysql_port" {
  value = "${aws_rds_cluster.mysql.port}"
}

output "mysql_security_group_id" {
  value = "${aws_security_group.mysql.id}"
}
