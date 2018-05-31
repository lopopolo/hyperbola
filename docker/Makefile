.PHONY: all
all:

.PHONY: build
build: build-mysql build-app build-fixtures

.PHONY: build-mysql
build-mysql:
	docker build --pull -f mysql/Dockerfile -t hyperbola-mysql mysql

.PHONY: build-app
build-app:
	docker build \
		--build-arg hyperbola_environment=local \
		--build-arg ansible_vault_password=$$(cd .. && dotenv get ANSIBLE_VAULT_PASSWORD) \
		--pull \
		-f app/Dockerfile -t hyperbola-app ..

.PHONY: build-fixtures
build-fixtures:
	docker build -f fixtures/Dockerfile -t hyperbola-fixtures fixtures

.PHONY: dev
dev: fixtures app

.PHONY: mysql
mysql: DOCKER_OPTS := \
	-e MYSQL_RANDOM_ROOT_PASSWORD=1 \
	-e MYSQL_DATABASE=hyperbola \
	-e MYSQL_USER=$(shell cd .. && dotenv get DB_USER | cut -d= -f 2) \
	-e MYSQL_PASSWORD=$(shell cd .. && dotenv get DB_PASSWORD | cut -d= -f 2)
mysql:
	@env HYP_SLEEP=10 HYP_DOCKER_OPTS="$(DOCKER_OPTS)" bin/launch-named-container mysql-docker hyperbola-mysql:latest

.PHONY: migrate
migrate:
	docker run --network hyperbola -d \
		--entrypoint /opt/venv/bin/python \
		-t hyperbola-app:latest \
		/opt/manage.py migrate

.PHONY: fixtures
fixtures: DOCKER_OPTS := \
	-e AWS_ACCESS_KEY_ID=$(shell aws --profile default configure get aws_access_key_id) \
	-e AWS_SECRET_ACCESS_KEY=$(shell aws --profile default configure get aws_secret_access_key)
fixtures: mysql migrate
	@env HYP_DOCKER_OPTS="$(DOCKER_OPTS)" bin/launch-named-container fixtures-docker hyperbola-fixtures:latest

.PHONY: app
app: DOCKER_OPTS := \
	-e AWS_ACCESS_KEY_ID=$(shell aws --profile default configure get aws_access_key_id) \
	-e AWS_SECRET_ACCESS_KEY=$(shell aws --profile default configure get aws_secret_access_key) \
	-p 8009:8000
app:
	@env HYP_DOCKER_OPTS="$(DOCKER_OPTS)" bin/launch-named-container app-docker hyperbola-app:latest

.PHONY: stop
stop:
	docker stop mysql-docker app-docker
