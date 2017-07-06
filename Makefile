.PHONY: hooks install_roles upgrade-py-deps

SHELL := /bin/bash

all: lint

## Tunnel

SSH_APP := vagrant ssh app-test-1

tunnel:
ifneq ("$(shell [[ -S ".vagrant/control-socket" ]] && echo "present" || echo)", "")
	@echo "Tunnel already established"
else
	$(SSH_APP) -- -M -S .vagrant/control-socket -fnNT -R 3306:localhost:3306
endif

tunnel-status:
ifeq ("$(shell [[ -S ".vagrant/control-socket" ]] && echo "present" || echo)", "")
	@echo "No control socket"
else
	$(SSH_APP) -- -S .vagrant/control-socket -O check
endif

tunnel-kill:
ifeq ("$(shell [[ -S ".vagrant/control-socket" ]] && echo "present" || echo)", "")
	@echo "No control socket"
else
	$(SSH_APP) -- -S .vagrant/control-socket -O exit
endif

## Lint

lint:
	ansible-playbook -i "localhost," ansible/provision.yml --syntax-check
	ansible-playbook -i "localhost," ansible/wiki.yml --syntax-check --vault-password-file=.secrets/vault-password.txt
	ansible-playbook -i "localhost," ansible/app.yml --syntax-check --vault-password-file=.secrets/vault-password.txt
	./venv/bin/ansible-lint --exclude=ansible/roles/geerlingguy.ruby --exclude=ansible/roles/geerlingguy.security --exclude=ansible/roles/hswong3i.tzdata ansible/provision.yml
	./venv/bin/ansible-lint --exclude=ansible/roles/geerlingguy.ruby --exclude=ansible/roles/geerlingguy.security --exclude=ansible/roles/hswong3i.tzdata ansible/wiki.yml

hooks:
	pre-commit install

install_roles:
	ansible-galaxy install -r ansible/roles/requirements.yml -p ansible/roles/ --force

## Virtualenv

upgrade-py-deps: requirements.in
	for req in $^; do CUSTOM_COMPILE_COMMAND="make $@" pip-compile --upgrade "$$req"; done
	$(MAKE) virtualenv

requirements.txt: requirements.in
	./venv/bin/pip-compile $<

virtualenv: venv/bin/activate

venv/bin/activate: requirements.txt
	virtualenv --python=python2 venv
	./venv/bin/pip install -U virtualenv pip pip-tools wheel setuptools
	./venv/bin/pip-sync $<
