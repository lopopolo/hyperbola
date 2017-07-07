terraform {
  required_version = "> 0.9.7"

  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/hyperbola-linode/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

variable "cloudflare_email" {
  default = "rjl@hyperbo.la"
}

variable "cloudflare_token" {
  default = ""
}

provider "cloudflare" {
  email = "${var.cloudflare_email}"
  token = "${coalesce(var.cloudflare_token, trimspace(file("${path.root}/../../../.secrets/cloudflare-api-key.txt")))}"
}

module "hyperbola-app" {
  source       = "../../hyperbola/app"
  host         = "hyperbola3"
  ipv4_address = "69.164.208.10"
  ipv6_address = "2600:3c03::f03c:91ff:fe2c:b8c8"
}

module "hyperbola-cdn" {
  source       = "../../hyperbola/cdn"
  host         = "hyperbola3"
  ipv4_address = "69.164.208.10"
  ipv6_address = "2600:3c03::f03c:91ff:fe2c:b8c8"
}
