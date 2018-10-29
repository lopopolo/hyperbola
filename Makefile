SHELL := /bin/bash
export PATH := ./venv/bin:$(PATH)

.PHONY: all
all:

## Development environment

.PHONY: dev-bootstrap
dev-bootstrap: hooks virtualenv

.PHONY: hooks
hooks:
	pre-commit install
	pre-commit install-hooks

.PHONY: install_roles
install_roles:
	ansible-galaxy install -r ansible/roles/requirements.yml -p ansible/roles/ --force

.PHONY: fixtures
fixtures:
	vagrant provision --provision-with fixtures app-local

## Release

.PHONY: release
release:
	bumpversion minor

.PHONY: build-ami
build-ami:
	env $$(dotenv get ANSIBLE_VAULT_PASSWORD) packer build packer/app.json

## Virtualenv

.PHONY: virtualenv
virtualenv: venv/bin/activate Pipfile
	VIRTUAL_ENV=venv pipenv install --dev

venv/bin/activate:
	python3 -m venv venv
	venv/bin/pip install -U pip setuptools pipenv

## clean

.PHONY: clean
clean: clean-pyc
	find . -name '.DS_Store' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
