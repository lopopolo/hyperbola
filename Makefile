SHELL := /bin/bash
export PATH := $(shell npm bin):./virtualenv/bin:$(PATH)

all: lint

## Linters

lint: flake8 isort pylint

flake8:
	-flake8 app

isort:
	-isort -rc app

pylint:
	-pylint --load-plugins pylint_django --reports=no --rcfile setup.cfg app/hyperbola

## Virtualenv

virtualenv:
	virtualenv --python=python3 virtualenv
	pip install -U virtualenv pip wheel setuptools
	pip install -r dev-requirements.txt --ignore-installed


wipe-virtualenv:
	rm -rf ./virtualenv
	git checkout -- virtualenv

## Node tools

css:
	postcss --use autoprefixer --use stylefmt --use colorguard --replace app/hyperbola/static/css/sitewide.css

.PHONY: flake8 isort pylint virtualenv wipe-virtualenv css

