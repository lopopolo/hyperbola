variable "env" {
}

variable "secret_key" {
}

variable "database_password" {
}

resource "aws_ssm_parameter" "secret_key" {
  name        = "/app/${var.env}/SECRET_KEY"
  description = "Django secret key"
  type        = "SecureString"
  value       = var.secret_key

  tags = {
    Environment = var.env
    Project     = "app"
  }
}

resource "aws_ssm_parameter" "database_password" {
  name        = "/app/${var.env}/DB_PASSWORD"
  description = "App database password"
  type        = "SecureString"
  value       = var.database_password

  tags = {
    Environment = var.env
    Project     = "app"
  }
}
