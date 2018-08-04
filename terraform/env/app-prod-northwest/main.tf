variable "name" {
  default = "app-prod-northwest"
}

variable "env" {
  default = "production"
}

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

module "hyperbola-app-base" {
  source = "../../hyperbola/app/base"
  env    = "${var.env}"
  bucket = "www"
}

module "hyperbola-app-mysql" {
  source = "../../hyperbola/app/mysql"
  env    = "${var.env}"
  name   = "${var.name}-mysql"

  vpc_id = "${module.network.vpc_id}"
  azs    = "${var.azs}"

  database_password = "${var.app_database_password}"
}

module "hyperbola-app-backend" {
  source   = "../../hyperbola/app/backend"
  name     = "${var.name}"
  env      = "${var.env}"
  key_name = ""

  vpc_id              = "${module.network.vpc_id}"
  public_subnet_tier  = "${module.network.public_subnet_tier}"
  private_subnet_tier = "${module.network.private_subnet_tier}"

  iam_instance_profile       = "${module.hyperbola-app-base.app_instance_profile}"
  s3_endpoint_prefix_list_id = "${module.network.s3_endpoint_prefix_list_id}"

  mysql_port              = "${module.hyperbola-app-mysql.mysql_port}"
  mysql_security_group_id = "${module.hyperbola-app-mysql.mysql_security_group_id}"
}

output "mysql_endpoint" {
  value = "${module.hyperbola-app-mysql.mysql_endpoint}"
}

output "backup_bucket" {
  value = "${module.hyperbola-app-base.backup_bucket}"
}

output "media_bucket" {
  value = "${module.hyperbola-app-base.media_bucket}"
}

output "backend_alb_dns" {
  value = "${module.hyperbola-app-backend.alb_dns}"
}
