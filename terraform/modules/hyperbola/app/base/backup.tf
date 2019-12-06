resource "aws_s3_bucket" "backup" {
  bucket = "hyperbola-app-backup-${var.env}"
  acl    = "private"

  tags = {
    Environment = var.env
  }
}

output "backup_bucket" {
  value = aws_s3_bucket.backup.bucket
}

output "backup_bucket_arn" {
  value = aws_s3_bucket.backup.arn
}
