.PHONY: install_roles

SHELL := /bin/bash

all: lint

lint:
	ansible-playbook -i "localhost," ansible/provision.yml --syntax-check
	ansible-playbook -i "localhost," ansible/wiki.yml --syntax-check --vault-password-file=.secrets/vault-password.txt
	./venv/bin/ansible-lint --exclude=ansible/roles/ansible-security --exclude=ansible/roles/ansible-tzdata --exclude=ansible/roles/ruby ansible/provision.yml
	./venv/bin/ansible-lint --exclude=ansible/roles/ansible-security --exclude=ansible/roles/ansible-tzdata --exclude=ansible/roles/ruby ansible/wiki.yml

hooks:
	pre-commit install

install_roles:
	ansible-galaxy install -r ansible/roles/requirements.yml -p ansible/roles/ --force

## Virtualenv

requirements.txt: requirements.in
	./venv/bin/pip-compile $<

virtualenv: venv/bin/activate

venv/bin/activate: requirements.txt
	virtualenv --python=python2 venv
	./venv/bin/pip install -U virtualenv pip pip-tools wheel setuptools
	./venv/bin/pip-sync $<
