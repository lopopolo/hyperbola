terraform {
  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/state-infra/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

resource "aws_s3_bucket" "hyperbola_terraform_state" {
  bucket = "hyperbola-terraform-state"
  acl    = "private"

  versioning {
    enabled    = true
    mfa_delete = false
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "aws:kms"
      }
    }
  }

  lifecycle {
    prevent_destroy = true
  }

  tags = {
    project    = "remote-state"
    managed_by = "terraform"
  }
}

resource "aws_s3_bucket_public_access_block" "hyperbola_terraform_state" {
  bucket = aws_s3_bucket.hyperbola_terraform_state.id

  block_public_acls   = true
  block_public_policy = true

  ignore_public_acls = true

  restrict_public_buckets = true
}

resource "aws_dynamodb_table" "terraform_statelock" {
  name           = "terraform_statelock"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "LockID"

  server_side_encryption {
    enabled = true
  }

  attribute {
    name = "LockID"
    type = "S"
  }

  lifecycle {
    prevent_destroy = true
  }

  tags = {
    project    = "remote-state"
    managed_by = "terraform"
  }
}
