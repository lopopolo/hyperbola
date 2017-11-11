# G Suite MX record values: https://support.google.com/a/answer/174125?hl=en
# G Suite TXT record values: https://support.google.com/a/answer/2716802?hl=en

resource "aws_route53_record" "hyperbola-MX" {
  zone_id = "${aws_route53_zone.hyperbola-zone.zone_id}"
  name    = "${aws_route53_zone.hyperbola-zone.name}"
  type    = "MX"
  ttl     = "300"

  records = [
    "1 ASPMX.L.GOOGLE.COM.",
    "5 ALT1.ASPMX.L.GOOGLE.COM.",
    "5 ALT2.ASPMX.L.GOOGLE.COM.",
    "10 ALT3.ASPMX.L.GOOGLE.COM.",
    "10 ALT4.ASPMX.L.GOOGLE.COM.",
  ]
}

resource "aws_route53_record" "hyperbola-google-site-verification-spf" {
  zone_id = "${aws_route53_zone.hyperbola-zone.zone_id}"
  name    = "${aws_route53_zone.hyperbola-zone.name}"
  type    = "TXT"
  ttl     = "300"

  records = [
    "v=spf1 include:_spf.google.com ~all",
    "google-site-verification=Kt2HDssbfMv5OIL422wGGexn00n1W4nTAZZTfUkyig8",
    "google-site-verification=vBbksaHJiPR9xr5eyVdQdvvIixg9di8BLwku3Sr1KCU",
  ]
}

resource "aws_route53_record" "hyperbola-dkim" {
  zone_id = "${aws_route53_zone.hyperbola-zone.zone_id}"
  name    = "google._domainkey"
  type    = "TXT"
  ttl     = "300"

  records = [
    "v=DKIM1; k=rsa;\" \"p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAk+xt4FleDx6/2ZY0vsfQCFY7Zh9v6EeXRWdw8Vqw88Dg+h1gpdB85722M2gITZFMAdrpXkxRQ89YQgrVfEitaLbaI74UCbeIBn6f+y+UNnS0RSimmqJTFyvFJTsEBway2QGFeZiRpYvXZAYsEsTwEyNwKz/7uRQSTKrua6r0rsooqK7auNn+YRmcNJJ3uOcPZrUnx4punYaFDd/n\" \"aa1Eo9nXKFemHHT6eLc620FWC+/MJWIlRFugsKPoiKu+0uAD0/EHE7x/5DwjrTutVLnuKlOA7tCHL0kir2f8wUOv0KRnC94G8hGl6nVML5iVk3So6SwFeovSkkM7tEUAL+4q6QIDAQAB",
  ]
}

resource "aws_route53_record" "hyperbolausercontent-net-MX" {
  zone_id = "${aws_route53_zone.hyperbolausercontent-net-public.zone_id}"
  name    = "${aws_route53_zone.hyperbolausercontent-net-public.name}"
  type    = "MX"
  ttl     = "300"

  records = [
    "1 ASPMX.L.GOOGLE.COM.",
    "5 ALT1.ASPMX.L.GOOGLE.COM.",
    "5 ALT2.ASPMX.L.GOOGLE.COM.",
    "10 ALT3.ASPMX.L.GOOGLE.COM.",
    "10 ALT4.ASPMX.L.GOOGLE.COM.",
  ]
}

resource "aws_route53_record" "hyperbolausercontent-net-google-site-verification-spf" {
  zone_id = "${aws_route53_zone.hyperbolausercontent-net-public.zone_id}"
  name    = "${aws_route53_zone.hyperbolausercontent-net-public.name}"
  type    = "TXT"
  ttl     = "300"

  records = [
    "v=spf1 include:_spf.google.com ~all",
    "google-site-verification=BAsDzAuut0wmAAA4v5iVIiTCWFYu0gLTvkK_sRk5O8Y",
  ]
}

resource "aws_route53_record" "hyperbolausercontent-net-dkim" {
  zone_id = "${aws_route53_zone.hyperbolausercontent-net-public.zone_id}"
  name    = "google._domainkey"
  type    = "TXT"
  ttl     = "300"

  records = [
    "v=DKIM1; k=rsa;\" \"p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm4qyzPNyrtbwcK/VmQn5a1lyW9pvE3Y5caL55A2Bg72goVGjGbGHmWrNW8dJJi/JSxWUJoyglSN9s3Ms1XjbBnzC9f3N/8CyRUtgZRAGuJCkrFOSdT4rZdjMp3UMottDDNtc6ziW6YRtQFHZ4b7IDFjs7tcupaM9LIVB4BKvMM5AwA9079gKRB7+vOOnNClq6qzVtnC8ttS9rcRY\" \"S7/rAambbT4/70MfEuTXpOCoV/TlUfFsP4Jsn85SXRKYUyL2Umk6fxwjKkzb3O7PI4/nQ/cn8lH0FJiAAhlaRSFkVZHMZr/XDlqdJw41VYzUuaDf0e9mpyCHXgTlvtQht0JJ/wIDAQAB",
  ]
}

resource "aws_route53_record" "hyperboladc-net-MX" {
  zone_id = "${aws_route53_zone.hyperboladc-net-public.zone_id}"
  name    = "${aws_route53_zone.hyperboladc-net-public.name}"
  type    = "MX"
  ttl     = "300"

  records = [
    "1 ASPMX.L.GOOGLE.COM.",
    "5 ALT1.ASPMX.L.GOOGLE.COM.",
    "5 ALT2.ASPMX.L.GOOGLE.COM.",
    "10 ALT3.ASPMX.L.GOOGLE.COM.",
    "10 ALT4.ASPMX.L.GOOGLE.COM.",
  ]
}

resource "aws_route53_record" "hyperboldc-net-google-site-verification-spf" {
  zone_id = "${aws_route53_zone.hyperboladc-net-public.zone_id}"
  name    = "${aws_route53_zone.hyperboladc-net-public.name}"
  type    = "TXT"
  ttl     = "300"

  records = [
    "v=spf1 include:_spf.google.com ~all",
    "google-site-verification=MBJltQtisR_DfhKzGfjs4mjMRpPK-1nRugHrza1elAA",
  ]
}

resource "aws_route53_record" "hyperboladc-net-dkim" {
  zone_id = "${aws_route53_zone.hyperboladc-net-public.zone_id}"
  name    = "google._domainkey"
  type    = "TXT"
  ttl     = "300"

  records = [
    "v=DKIM1; k=rsa;\" \"p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgw9GWNAV7pI++w0j2kBrSkZbU9+v0cULWem5c1n2AavdmSp+JP0WNXww3bi72pxI2Vrq0iTlmSVxERCLMhnHx1jHEg+iz/JsngVF9ShSYHfs0oz89hVGzA9nX/pC+DH0r066BHtB5DiTcH5MHLLcMjJMjHbw6C/LnAygUMac4pGPlaj56V+TTZpr/dEm5zkzhb+i500SROmnwAy5\" \"CsCymPXE3jcoOLeCh1MkJGZgH7hxgBxusii3Z1jvtVHodRWXp7P2UYmHJTCWtTpCribewkRluRGsNao5Ssxtql+16PqNJzY/VpeW1G9Qv77KS9iBZvQpCXALAZnfU637UoNKxwIDAQAB",
  ]
}
