SHELL := /bin/bash
export PATH := ./virtualenv/bin:$(PATH)

all: lint

## Linters

lint: flake8 isort pylint

flake8:
	-flake8 app

isort:
	-isort -rc app

pylint:
	-pylint --load-plugins pylint_django --rcfile setup.cfg app/hyperbola

## Virtualenv

virtualenv:
	virtualenv --python=python3 virtualenv
	pip install -U virtualenv pip wheel setuptools
	pip install -r dev-requirements.txt --ignore-installed


wipe-virtualenv:
	rm -rf ./virtualenv
	git checkout -- virtualenv

.PHONY: flake8 isort pylint virtualenv wipe-virtualenv

