.PHONY: install_roles

SHELL := /bin/bash
export PATH := ./venv/bin:$(PATH)

all: lint

lint:
	ansible-playbook -i "localhost," ansible/provision.yml --syntax-check
	ansible-playbook -i "localhost," ansible/wiki.yml --syntax-check --vault-password-file=.secrets/vault-password.txt
	ansible-lint --exclude=ansible/roles/ansible-security --exclude=ansible/roles/ansible-tzdata --exclude=roles/ruby ansible/provision.yml
	ansible-lint --exclude=ansible/roles/ansible-security --exclude=ansible/roles/ansible-tzdata --exclude=ansible/roles/ruby ansible/wiki.yml

hooks:
	venv/bin/pre-commit install

install_roles:
	ansible-galaxy install -r roles/requirements.yml -p ./roles/ --force

virtualenv: wipe-virtualenv
	virtualenv --python=$$(which python2) venv
	pip install -U virtualenv pip wheel setuptools
	pip install -r requirements.txt --ignore-installed


wipe-virtualenv:
	rm -rf ./venv
