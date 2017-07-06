module "local" {
  source        = "./env"
  env           = "local"
  bucket        = "local"
  redis         = "app.local.hyperboladc.net"
  backup_s3_arn = "${aws_s3_bucket.backup.arn}"
}
