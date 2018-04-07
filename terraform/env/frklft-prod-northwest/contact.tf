variable "contact_email" {}
variable "recaptcha_secret_key" {}

resource "aws_cloudformation_stack" "contact-form" {
  name         = "FRKLFT-Contact-Us"
  capabilities = ["CAPABILITY_IAM"]

  parameters {
    ToEmailAddress  = "${var.contact_email}"
    ReCaptchaSecret = "${var.recaptcha_secret_key}"
  }

  template_body = "${file("${path.module}/contact-form-cloudformation-stack.yml")}"
}

output "contact_api_url" {
  value = "${aws_cloudformation_stack.contact-form.outputs["ApiUrl"]}"
}
