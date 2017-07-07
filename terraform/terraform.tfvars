#--------------------------------------------------------------
# General
#--------------------------------------------------------------

name              = "hyperbola"
region            = "us-east-1"
iam_admins        = "hyperbola-admin" # Comma separated list of admins (e.g. cameron,jay,jon,kevin)

#--------------------------------------------------------------
# Network
#--------------------------------------------------------------

vpc_cidr        = "10.139.0.0/16"
azs             = "us-east-1a,us-east-1c,us-east-1e" # AZs are region specific

# Bastion
bastion_instance_type = "t2.micro"
