terraform {
  required_version = "> 0.9.7"

  backend "s3" {
    bucket         = "hyperbola-terraform-state"
    region         = "us-east-1"
    key            = "terraform/wr-prod-northwest/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "terraform_statelock"
  }
}

resource "aws_s3_bucket" "website" {
  bucket = "www.burnfastburnbright.com"
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}

resource "aws_s3_bucket_object" "index" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "index.html"
  source       = "${path.root}/site/index.html"
  etag         = "${md5(file("${path.root}/site/index.html"))}"
  content_type = "text/html"
}

resource "aws_s3_bucket_object" "error" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "error.html"
  source       = "${path.root}/site/index.html"
  etag         = "${md5(file("${path.root}/site/index.html"))}"
  content_type = "text/html"
}

resource "aws_s3_bucket_object" "image" {
  bucket       = "${aws_s3_bucket.website.id}"
  acl          = "public-read"
  key          = "WR-124.jpg"
  source       = "${path.root}/site/WR-124.jpg"
  etag         = "${md5(file("${path.root}/site/WR-124.jpg"))}"
  content_type = "image/jpeg"
}
