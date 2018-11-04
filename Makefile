.PHONY: all
all:

## Development environment

.PHONY: dev-bootstrap
dev-bootstrap: hooks virtualenv

.PHONY: hooks
hooks:
	pre-commit install
	pre-commit install-hooks

.PHONY: fixtures
fixtures:
	vagrant provision --provision-with fixtures app-local

## Release

.PHONY: release
release:
	venv/bin/bumpversion minor

.PHONY: build-ami
build-ami:
	bin/dotenv-exec packer build packer/app.json

## Virtualenv

.PHONY: virtualenv
virtualenv: venv/bin/activate Pipfile
	VIRTUAL_ENV=venv pipenv install --dev

venv/bin/activate:
	python3 -m venv venv
	venv/bin/pip install -U pip setuptools pipenv

## clean

.PHONY: clean
clean:
	@find . -name '.DS_Store' -delete
	@rm -rf *.egg *.egg-info .cache .coverage .tox build dist docs/build htmlcov
	@find . -type d -name __pycache__ -exec rm -rf {} \;
	@find . -type f -name '*.pyc' -or -name '*.pyo' -delete
