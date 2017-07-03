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

build: clean-build
	./bin/artifact-exec gulp
	./bin/artifact-exec webpack -p

## Linters

lint: lint-py

lint-py: flake8 isort pep257 pylint

flake8:
	flake8 app bin

isort:
	isort --apply --recursive app bin

pep257:
	pep257 app bin

pylint:
	pylint --rcfile setup.cfg app bin

# must manually run and compare `git diff` output
yapf:
	-yapf --exclude '*/migrations/*' -i --recursive app/hyperbola/

## Virtualenv

upgrade-py-deps: requirements.in dev-requirements.in
	for req in $^; do CUSTOM_COMPILE_COMMAND="make $@" pip-compile --upgrade "$$req"; done
	$(MAKE) virtualenv

requirements.txt: requirements.in
	pip-compile $<

dev-requirements.txt: dev-requirements.in requirements.txt
	pip-compile $<

virtualenv: virtualenv/bin/activate

virtualenv/bin/activate: dev-requirements.txt requirements.txt
	python -m venv virtualenv
	pip install -U virtualenv pip pip-tools wheel setuptools
	pip-sync $<

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

clean-build:
	./bin/artifact-exec gulp clean

.PHONY: flake8 isort pep257 pylint yapf \
	upgrade-py-deps \
	build \
	clean clean-pyc clean-assets clean-build

