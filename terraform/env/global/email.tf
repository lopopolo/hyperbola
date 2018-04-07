module "hyperbola-email-dns" {
  source = "../../hyperbola/gsuite/email-dns"

  zone_id                      = "${aws_route53_zone.hyperbola-zone.zone_id}"
  zone_name                    = "${aws_route53_zone.hyperbola-zone.name}"
  google_site_verifcation_keys = "Kt2HDssbfMv5OIL422wGGexn00n1W4nTAZZTfUkyig8,vBbksaHJiPR9xr5eyVdQdvvIixg9di8BLwku3Sr1KCU"
  dkim                         = "p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAk+xt4FleDx6/2ZY0vsfQCFY7Zh9v6EeXRWdw8Vqw88Dg+h1gpdB85722M2gITZFMAdrpXkxRQ89YQgrVfEitaLbaI74UCbeIBn6f+y+UNnS0RSimmqJTFyvFJTsEBway2QGFeZiRpYvXZAYsEsTwEyNwKz/7uRQSTKrua6r0rsooqK7auNn+YRmcNJJ3uOcPZrUnx4punYaFDd/naa1Eo9nXKFemHHT6eLc620FWC+/MJWIlRFugsKPoiKu+0uAD0/EHE7x/5DwjrTutVLnuKlOA7tCHL0kir2f8wUOv0KRnC94G8hGl6nVML5iVk3So6SwFeovSkkM7tEUAL+4q6QIDAQAB"
}

module "hyperbolausercontent-email-dns" {
  source = "../../hyperbola/gsuite/email-dns"

  zone_id                      = "${aws_route53_zone.hyperbolausercontent-net-public.zone_id}"
  zone_name                    = "${aws_route53_zone.hyperbolausercontent-net-public.name}"
  google_site_verifcation_keys = "BAsDzAuut0wmAAA4v5iVIiTCWFYu0gLTvkK_sRk5O8Y"
  dkim                         = "p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm4qyzPNyrtbwcK/VmQn5a1lyW9pvE3Y5caL55A2Bg72goVGjGbGHmWrNW8dJJi/JSxWUJoyglSN9s3Ms1XjbBnzC9f3N/8CyRUtgZRAGuJCkrFOSdT4rZdjMp3UMottDDNtc6ziW6YRtQFHZ4b7IDFjs7tcupaM9LIVB4BKvMM5AwA9079gKRB7+vOOnNClq6qzVtnC8ttS9rcRYS7/rAambbT4/70MfEuTXpOCoV/TlUfFsP4Jsn85SXRKYUyL2Umk6fxwjKkzb3O7PI4/nQ/cn8lH0FJiAAhlaRSFkVZHMZr/XDlqdJw41VYzUuaDf0e9mpyCHXgTlvtQht0JJ/wIDAQAB"
}

module "hyperboladc-email-dns" {
  source = "../../hyperbola/gsuite/email-dns"

  zone_id                      = "${aws_route53_zone.hyperboladc-net-public.zone_id}"
  zone_name                    = "${aws_route53_zone.hyperboladc-net-public.name}"
  google_site_verifcation_keys = "MBJltQtisR_DfhKzGfjs4mjMRpPK-1nRugHrza1elAA"
  dkim                         = "p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgw9GWNAV7pI++w0j2kBrSkZbU9+v0cULWem5c1n2AavdmSp+JP0WNXww3bi72pxI2Vrq0iTlmSVxERCLMhnHx1jHEg+iz/JsngVF9ShSYHfs0oz89hVGzA9nX/pC+DH0r066BHtB5DiTcH5MHLLcMjJMjHbw6C/LnAygUMac4pGPlaj56V+TTZpr/dEm5zkzhb+i500SROmnwAy5CsCymPXE3jcoOLeCh1MkJGZgH7hxgBxusii3Z1jvtVHodRWXp7P2UYmHJTCWtTpCribewkRluRGsNao5Ssxtql+16PqNJzY/VpeW1G9Qv77KS9iBZvQpCXALAZnfU637UoNKxwIDAQAB"
}
