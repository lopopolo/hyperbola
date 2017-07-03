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
private_subnets = "10.139.1.0/24,10.139.2.0/24,10.139.3.0/24" # Creating one private subnet per AZ
public_subnets  = "10.139.11.0/24,10.139.12.0/24,10.139.13.0/24" # Creating one public subnet per AZ

# Bastion
bastion_instance_type = "t2.micro"
