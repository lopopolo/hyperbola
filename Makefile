SHELL := ./bin/artifact-exec /bin/bash

.PHONY: all
all: lint build

## Development environment

.PHONY: hooks
hooks:
	pre-commit install

.PHONY: yarn-dist-update
yarn-dist-update:
	rm -rf ./bin/dist
	wget -O- https://yarnpkg.com/latest.tar.gz | tar zvx -C ./bin
	echo '*' > ./bin/dist/.gitignore

## Build

.PHONY: build
build:
	gulp

.PHONY: release
release:
	bumpversion minor

## Linters

.PHONY: lint
lint: lint-py lint-js

.PHONY: lint-py
lint-py: flake8 isort pep257 pylint

.PHONY: flake8
flake8:
	flake8 app bin *.py

.PHONY: isort
isort:
	isort --apply --recursive app bin *.py

.PHONY: pep257
pep257:
	pep257 app bin *.py

.PHONY: pylint
pylint:
	pylint --rcfile setup.cfg app bin *.py

# must manually run and compare `git diff` output
.PHONY: yapf
yapf:
	-yapf --exclude '*/migrations/*' -i --recursive app/hyperbola/

.PHONY: lint-js
lint-js: $(wildcard *.js)
	eslint $^

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

virtualenv: virtualenv/bin/activate

virtualenv/bin/activate: dev-requirements.txt requirements.txt
	python -m venv virtualenv
	pip install -U virtualenv pip pip-tools wheel setuptools
	pip-sync $^

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
