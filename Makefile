.PHONY: install_roles

SHELL := /bin/bash
export PATH := ./venv/bin:$(PATH)

all: lint

lint:
	ansible-lint provision.yml
	ansible-lint wiki.yml

install_roles:
	ansible-galaxy install -r roles/requirements.yml -p ./roles/ --force

virtualenv: wipe-virtualenv
	virtualenv --python=$$(which python2) venv
	pip install -U virtualenv pip wheel setuptools
	pip install -r requirements.txt --ignore-installed


wipe-virtualenv:
	rm -rf ./venv
