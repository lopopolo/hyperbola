#!/bin/bash

set -e
set -x

define(){ IFS='\n' read -r -d '' $${1} || true; }

define ANSIBLE_VAULT_PASSWORD <<'EOF'
${ansible_vault_password}
EOF

# install ansible
apt-get install software-properties-common
apt-add-repository -y ppa:ansible/ansible
apt-get update
apt-get install -y ansible git

cd /tmp
git clone https://github.com/lopopolo/hyperbola-tools.git
cd hyperbola-tools

echo $ANSIBLE_VAULT_PASSWORD > vault-password.txt

ansible-playbook --connection=local --inventory-file=./production.ini provision.yml
ansible-playbook --connection=local --inventory-file=./production.ini --vault-password-file=./vault-password.txt -v wiki.yml

cd /tmp
rm -rf /tmp/hyperbola-tools

exit 0
