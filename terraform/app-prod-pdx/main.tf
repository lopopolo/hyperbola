variable "name" {
  default = "app-prod-northwest"
}

variable "env" {
  default = "production"
}

variable "app_secret_key" {}

variable "app_database_password" {}

terraform {
  required_version = "> 0.9.7"

  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/app-prod-northwest/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

module "base" {
  source = "../modules/hyperbola/app/base"
  env    = "${var.env}"
  bucket = "www"
}

module "secrets" {
  source = "../modules/hyperbola/app/secrets"
  env    = "${var.env}"

  secret_key        = "${var.app_secret_key}"
  database_password = "${var.app_database_password}"
}

module "mysql" {
  source = "../modules/hyperbola/app/mysql"
  env    = "${var.env}"
  name   = "${var.name}-mysql"

  vpc_id = "${module.network.vpc_id}"
  azs    = "${var.azs}"

  database_password = "${var.app_database_password}"
}

module "backend" {
  source   = "../modules/hyperbola/app/backend"
  name     = "${var.name}"
  env      = "${var.env}"
  key_name = ""

  vpc_id              = "${module.network.vpc_id}"
  public_subnet_tier  = "${module.network.public_subnet_tier}"
  private_subnet_tier = "${module.network.private_subnet_tier}"

  iam_instance_profile       = "${module.base.app_instance_profile}"
  s3_endpoint_prefix_list_id = "${module.network.s3_endpoint_prefix_list_id}"

  mysql_port              = "${module.mysql.port}"
  mysql_security_group_id = "${module.mysql.security_group_id}"
}

output "mysql_endpoint" {
  value = "${module.mysql.endpoint}"
}

output "backup_bucket" {
  value = "${module.base.backup_bucket}"
}

output "media_bucket" {
  value = "${module.base.media_bucket}"
}

output "backend_alb_dns" {
  value = "${module.backend.alb_dns}"
}
