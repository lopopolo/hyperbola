all: lint

lint: flake8 isort pylint

flake8:
	-./virtualenv/bin/flake8 app

isort:
	-./virtualenv/bin/isort -rc app

pylint:
	-./virtualenv/bin/pylint --load-plugins pylint_django --rcfile setup.cfg app/hyperbola

virtualenv:
	virtualenv virtualenv
	./virtualenv/bin/pip install -U virtualenv pip wheel setuptools
	./virtualenv/bin/pip install -r dev-requirements.txt --ignore-installed


wipe-virtualenv:
	rm -rf ./virtualenv
	git checkout -- virtualenv

.PHONY: flake8 isort pylint virtualenv wipe-virtualenv

