SHELL := /bin/bash
export PATH := $(shell npm bin):./virtualenv/bin:$(PATH)

all: lint

## Linters

lint: eslint htmlhint flake8 isort pep257 pylint

eslint:
	eslint bin/*.html
	eslint app/hyperbola/static/js/lifestream-date-formatter.js

htmlhint:
	htmlhint bin/*.html

flake8:
	flake8 app
	flake8 bin

isort:
	isort --apply --recursive app
	isort --apply --recursive bin

pep257:
	pep257 app
	pep257 bin

pylint:
	pylint --rcfile setup.cfg app
	pylint --rcfile setup.cfg bin

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

## Code Generation

closure-compile:
	java -jar node_modules/google-closure-compiler/compiler.jar --language_out ECMASCRIPT5 \
		--compilation_level ADVANCED_OPTIMIZATIONS \
		--js app/hyperbola/static/js/lifestream-date-formatter.js \
		--js_output_file app/hyperbola/lifestream/templates/lifestream-date-formatter.generated.min.js

css:
	postcss --use autoprefixer --use stylefmt --use colorguard --replace app/hyperbola/static/css/sitewide.css
	purifycss app/hyperbola/static/vendor/bootstrap-css-only/css/bootstrap.css app/hyperbola/*/templates/*.html app/hyperbola/templates/*.html --info --out app/hyperbola/static/css/bootstrap.purified.css

## clean

clean: clean-pyc clean-assets

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-assets:
	find assets -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +

.PHONY: eslint htmlhint flake8 isort pep257 pylint yapf \
	virtualenv wipe-virtualenv \
	closure-compile css \
	clean clean-pyc clean-assets

