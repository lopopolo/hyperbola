resource "aws_s3_bucket" "backup" {
  bucket = "hyperbola-app-backup"
  acl    = "private"

  tags {
    Name = "hyperbola-app backup - all environments"
  }
}

output "backup_bucket_arn" {
  value = "${aws_s3_bucket.backup.arn}"
}
