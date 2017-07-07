terraform {
  required_version = "> 0.9.7"

  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/home-dc-infra/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

resource "aws_s3_bucket" "home-dc-hyperbola" {
  bucket = "home-dc-hyperbola"
  acl    = "private"

  versioning {
    enabled = true
  }

  lifecycle {
    prevent_destroy = true
  }

  lifecycle_rule {
    id      = "media-backup"
    prefix  = "/"
    enabled = true

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    noncurrent_version_transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    noncurrent_version_transition {
      days          = 60
      storage_class = "GLACIER"
    }
  }
}