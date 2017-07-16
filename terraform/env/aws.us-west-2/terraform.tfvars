#--------------------------------------------------------------
# General
#--------------------------------------------------------------

name              = "hyperbola-production-us-west-2"
region            = "us-west-2"

#--------------------------------------------------------------
# Network
#--------------------------------------------------------------

vpc_cidr        = "10.149.0.0/16"
azs             = "us-west-2a,us-west-2b,us-west-2c" # AZs are region specific

# Bastion
bastion_instance_type = "t2.nano"
