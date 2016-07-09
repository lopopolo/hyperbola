SHELL := /bin/bash
export PATH := $(shell npm bin):./virtualenv/bin:$(PATH)

all: lint

## Linters

lint: flake8 isort pylint

flake8:
	-flake8 app

isort:
	-isort --apply --recursive app

pylint:
	-pylint --rcfile setup.cfg app/hyperbola

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

## Node tools

css:
	postcss --use autoprefixer --use stylefmt --use colorguard --replace app/hyperbola/static/css/sitewide.css

## clean

clean: clean-pyc clean-assets

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-assets:
	find assets -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +

.PHONY: flake8 isort pylint yapf virtualenv wipe-virtualenv css clean clean-pyc clean-assets

