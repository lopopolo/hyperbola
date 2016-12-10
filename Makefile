SHELL := /bin/bash
export PATH := $(shell npm bin):./virtualenv/bin:$(PATH)

all: lint

hooks:
	virtualenv/bin/pre-commit install

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

virtualenv: wipe-virtualenv
	virtualenv --python=python3 virtualenv
	pip install -U virtualenv pip wheel setuptools
	pip install -r dev-requirements.txt --ignore-installed

wipe-virtualenv:
	rm -rf ./virtualenv
	git checkout -- virtualenv

## clean

clean: clean-pyc clean-assets

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-assets:
	find assets -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +

.PHONY: flake8 isort pep257 pylint yapf \
	virtualenv wipe-virtualenv \
	clean clean-pyc clean-assets

