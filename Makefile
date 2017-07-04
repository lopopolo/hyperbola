SHELL := /bin/bash
export PATH := ./virtualenv/bin:$(PATH)

PYTHON_VERSION := $(shell cat .python-version)

all: lint build

hooks:
	pre-commit install

yarn-update:
	rm -rf ./bin/dist
	wget -O- https://yarnpkg.com/latest.tar.gz | tar zvx -C ./bin
	echo '*' > ./bin/dist/.gitignore

## Build

build:
	./bin/artifact-exec gulp

release:
	bumpversion minor

## Linters

lint: lint-py lint-js

lint-py: flake8 isort pep257 pylint

flake8:
	flake8 app bin *.py

isort:
	isort --apply --recursive app bin *.py

pep257:
	pep257 app bin *.py

pylint:
	pylint --rcfile setup.cfg app bin *.py

# must manually run and compare `git diff` output
yapf:
	-yapf --exclude '*/migrations/*' -i --recursive app/hyperbola/

lint-js: $(wildcard *.js)
	./bin/artifact-exec eslint $^

## Virtualenv

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

clean: clean-pyc clean-assets
	find . -name '.DS_Store' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-assets:
	find assets -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +
	rm -f assets/staticfiles.json

.PHONY: flake8 isort pep257 pylint yapf \
	upgrade-py-deps \
	build \
	clean clean-pyc clean-assets

