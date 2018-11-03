#!/bin/bash -eux

# This script is based on packer-ubuntu-1604@f797d835
# <https://github.com/geerlingguy/packer-ubuntu-1604/blob/f797d835/scripts/cleanup.sh>
#
# MIT License
#
# Copyright (c) 2016, Jeff Geerling

# Uninstall Ansible and remove PPA.
apt -y remove --purge ansible
apt-add-repository --remove ppa:ansible/ansible

# Apt cleanup.
apt autoremove
apt update

# Delete unneeded files.
rm -f /tmp/vault-password.txt

# Zero out the rest of the free space using dd, then delete the written file.
dd if=/dev/zero of=/EMPTY bs=1M
rm -f /EMPTY

# Add `sync` so Packer doesn't quit too early, before the large file is deleted.
sync
