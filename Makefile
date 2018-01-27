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
	NODE_ENV="production" webpack -p

.PHONY: release
release:
	bumpversion minor

.PHONY: build-ami
build-ami:
	env $$(dotenv get ANSIBLE_VAULT_PASSWORD) packer build packer/app.json

## Linters

.PHONY: lint
lint: lint-pre-commit lint-ansible lint-git

.PHONY: lint-git
lint-git:
	git ls-files -i --exclude-standard
	[[ "$$(git ls-files -i --exclude-standard | wc -l | tr -d ' ')" == "0" ]]

PRE_COMMIT := pre-commit run --all-files

.PHONY: lint-pre-commit
lint-pre-commit:
	$(PRE_COMMIT) check-ast
	$(PRE_COMMIT) check-docstring-first
	$(PRE_COMMIT) check-executables-have-shebangs
	$(PRE_COMMIT) check-json
	$(PRE_COMMIT) check-yaml
	$(PRE_COMMIT) end-of-file-fixer
	$(PRE_COMMIT) flake8
	$(PRE_COMMIT) trailing-whitespace
	$(PRE_COMMIT) python-import-sorter
	$(PRE_COMMIT) pydocstyle
	$(PRE_COMMIT) pylint
	$(PRE_COMMIT) pyupgrade
	$(PRE_COMMIT) terraform_fmt
	$(PRE_COMMIT) eslint
	$(PRE_COMMIT) csslint
	$(PRE_COMMIT) shell-lint

ANSIBLE_LINT_EXCLUDE := --exclude=ansible/roles/geerlingguy.ntp \
	--exclude=ansible/roles/geerlingguy.security \
	--exclude=ansible/roles/hswong3i.tzdata \
	--exclude=ansible/roles/mprahl.lets-encrypt-route-53 \
	--exclude=ansible/lb-local.yml \
	--exclude=ansible/mysql-local.yml

.PHONY: lint-ansible
lint-ansible:
	ansible-playbook -i ansible/local.ini --syntax-check --vault-password-file=bin/ansible_vault_password.py ansible/*.yml
	ansible-lint $(ANSIBLE_LINT_EXCLUDE) ansible/roles/hyperbola*
	ansible-lint $(ANSIBLE_LINT_EXCLUDE) ansible/*.yml

## Virtualenv

.PHONY: virtualenv
virtualenv: venv/bin/activate Pipfile
	VIRTUAL_ENV=venv pipenv install --dev

venv/bin/activate:
	python -m venv venv

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
