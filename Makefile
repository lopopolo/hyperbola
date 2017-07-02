SHELL := /bin/bash
export PATH := ./virtualenv/bin:$(PATH)

PYTHON_VERSION := $(shell cat .python-version)

all: lint

hooks:
	pre-commit install

yarn-update:
	rm -rf ./bin/dist
	wget -O- https://yarnpkg.com/latest.tar.gz | tar zvx -C ./bin
	echo '*' > ./bin/dist/.gitignore

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
	for req in $^; do pip-compile --upgrade "$$req"; done
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

.PHONY: flake8 isort pep257 pylint yapf \
	upgrade-py-deps \
	clean clean-pyc clean-assets

