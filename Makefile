SHELL := /bin/bash
export PATH := ./bin:./venv/bin:$(shell yarn bin):$(PATH)

.PHONY: all
all: lint build

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

## Build

.PHONY: build
build:
	webpack --mode production

.PHONY: fixtures
fixtures:
	vagrant provision --provision-with fixtures app-local

.PHONY: release
release:
	bumpversion minor

.PHONY: build-ami
build-ami:
	env $$(dotenv get ANSIBLE_VAULT_PASSWORD) packer build packer/app.json

## Linters

.PHONY: lint
lint: lint-ansible lint-git

.PHONY: lint-git
lint-git:
	git ls-files -i --exclude-standard
	[[ "$$(git ls-files -i --exclude-standard | wc -l | tr -d ' ')" == "0" ]]

ANSIBLE_LINT_EXCLUDE := \
	--exclude=ansible/roles/hswong3i.tzdata \
	--exclude=ansible/roles/mprahl.lets-encrypt-route-53

.PHONY: lint-ansible
lint-ansible:
	ansible-playbook -i ansible/local.ini --syntax-check --vault-password-file=bin/ansible_vault_password.py ansible/*.yml
	ansible-lint $(ANSIBLE_LINT_EXCLUDE) ansible/*.yml

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
