SHELL := ./bin/artifact-exec bash

.PHONY: all
all: lint build

## Development environment

.PHONY: dev-bootstrap
dev-bootstrap: hooks yarn-dist-update virtualenv

.PHONY: hooks
hooks:
	pre-commit install

.PHONY: yarn-dist-update
yarn-dist-update:
	rm -rf ./bin/dist
	wget -O- https://yarnpkg.com/latest.tar.gz | tar zvx -C ./bin
	echo '*' > ./bin/dist/.gitignore

.PHONY: install_roles
install_roles:
	ansible-galaxy install -r ansible/roles/requirements.yml -p ansible/roles/ --force

## Build

.PHONY: build
build:
	NODE_ENV="production" gulp

.PHONY: release
release:
	bumpversion minor

## Linters

.PHONY: lint
lint: lint-pre-commit lint-ansible

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

# must manually run and compare `git diff` output
.PHONY: yapf
yapf:
	-yapf --exclude '*/migrations/*' -i --recursive app/hyperbola/

ANSIBLE_LINT_EXCLUDE := --exclude=ansible/roles/geerlingguy.ruby --exclude=ansible/roles/geerlingguy.security --exclude=ansible/roles/hswong3i.tzdata
lint-ansible:
	ansible-playbook -i "localhost," --syntax-check --vault-password-file=.secrets/vault-password.txt ansible/*.yml
	ansible-lint $(ANSIBLE_LINT_EXCLUDE) ansible/roles/hyperbola*
	ansible-lint $(ANSIBLE_LINT_EXCLUDE) ansible/*.yml
## Virtualenv

.PHONY: upgrade-py-deps
upgrade-py-deps: setup.py requirements.in dev-requirements.in
	for req in $^; do if [[ "$$req" != "setup.py" ]]; then CUSTOM_COMPILE_COMMAND="make $@" pip-compile --upgrade "$$req"; sed -i '' "s|-e file://$$(pwd)||" "$$(basename "$$req" ".in").txt"; fi; done
	$(MAKE) virtualenv

requirements.txt: requirements.in setup.py
	pip-compile --output-file "$@" "$<"
	sed -i '' "s|-e file://$$(pwd)||" "$@"

dev-requirements.txt: dev-requirements.in setup.py
	pip-compile --output-file "$@" "$<"
	sed -i '' "s|-e file://$$(pwd)||" "$@"

.PHONY: virtualenv
virtualenv: venv/bin/activate dev-requirements.txt requirements.txt
	pip-sync *requirements.txt

venv/bin/activate:
	python -m venv venv
	pip install -U virtualenv pip pip-tools wheel setuptools

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

## Tunnel

SSH_APP := vagrant ssh app-test-1

.PHONY: tunnel
tunnel:
ifneq ("$(shell [[ -S ".vagrant/control-socket" ]] && echo "present" || echo)", "")
	@echo "Tunnel already established"
else
	$(SSH_APP) -- -M -S .vagrant/control-socket -fnNT -R 3306:localhost:3306
endif

.PHONY: tunnel-status
tunnel-status:
ifeq ("$(shell [[ -S ".vagrant/control-socket" ]] && echo "present" || echo)", "")
	@echo "No control socket"
else
	$(SSH_APP) -- -S .vagrant/control-socket -O check
endif

.PHONY: tunnel-kill
tunnel-kill:
ifeq ("$(shell [[ -S ".vagrant/control-socket" ]] && echo "present" || echo)", "")
	@echo "No control socket"
else
	$(SSH_APP) -- -S .vagrant/control-socket -O exit
endif
