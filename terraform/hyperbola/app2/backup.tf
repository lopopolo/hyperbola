resource "aws_s3_bucket" "backup" {
  bucket = "hyperbola-app-backup"
  acl    = "private"

  tags {
    Name = "hyperbola-app backup - all environments"
  }
}
