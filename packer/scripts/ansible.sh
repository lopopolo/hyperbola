#!/bin/bash -eux

# This script is based on packer-ubuntu-1604@f797d835
# <https://github.com/geerlingguy/packer-ubuntu-1604/blob/f797d835/scripts/ansible.sh>
#
# MIT License
#
# Copyright (c) 2016, Jeff Geerling

# Install Ansible repository.
apt -y update
apt -y install software-properties-common
apt-add-repository ppa:ansible/ansible

# Install Ansible.
apt -y update
apt -y install ansible

# Setup vault password file.
printenv ANSIBLE_VAULT_PASSWORD > /tmp/vault-password.txt
