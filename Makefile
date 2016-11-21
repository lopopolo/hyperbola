.PHONY: install_roles

SHELL := /bin/bash
export PATH := ./venv/bin:$(PATH)

all: lint

lint:
	ansible-lint --exclude=roles/ansible-hostname --exclude=roles/ansible-security --exclude=roles/ansible-tzdata --exclude=roles/ruby provision.yml
	ansible-lint --exclude=roles/ansible-hostname --exclude=roles/ansible-security --exclude=roles/ansible-tzdata --exclude=roles/ruby wiki.yml

hooks:
	venv/bin/pre-commit install

install_roles:
	ansible-galaxy install -r roles/requirements.yml -p ./roles/ --force

# Ansible config
export ANSIBLE_CALLBACK_WHITELIST := profile_tasks

provision:
	 ansible-playbook --connection=ssh --timeout=30 --inventory-file=./production.ini --ask-become-pass -v provision.yml

wiki:
	ansible-playbook --connection=ssh --timeout=30 --inventory-file=./production.ini --ask-become-pass --ask-vault-pass -v wiki.yml

virtualenv: wipe-virtualenv
	virtualenv --python=$$(which python2) venv
	pip install -U virtualenv pip wheel setuptools
	pip install -r requirements.txt --ignore-installed


wipe-virtualenv:
	rm -rf ./venv
