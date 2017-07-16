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
