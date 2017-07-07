data "terraform_remote_state" "global" {
  backend = "s3"

  config {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/hyperbola-global/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

module "local" {
  source        = "./env"
  env           = "local"
  bucket        = "local"
  redis         = "app.local.hyperboladc.net"
  backup_s3_arn = "${data.terraform_remote_state.global.backup_bucket_arn}"
}
