.PHONY: all
all:

.PHONY: build
build: build-mysql build-app build-fixtures build-static

.PHONY: build-mysql
build-mysql:
	docker build --pull -f mysql/Dockerfile -t hyperbola/mysql mysql

.PHONY: build-app
build-app:
	docker build \
		--build-arg hyperbola_environment=local \
		--build-arg ansible_vault_password=$$(cd .. && dotenv get ANSIBLE_VAULT_PASSWORD) \
		--pull \
		-f app/Dockerfile -t hyperbola/app ..

.PHONY: build-fixtures
build-fixtures:
	docker build -f fixtures/Dockerfile -t hyperbola/fixtures fixtures

.PHONY: build-static
build-static:
	docker pull nginx:stable-alpine
	docker build -f static/Dockerfile -t hyperbola/static ..

.PHONY: dev
dev: mysql migrate fixtures app static

.PHONY: mysql
mysql: DOCKER_OPTS := \
	-e MYSQL_RANDOM_ROOT_PASSWORD=1 \
	-e MYSQL_DATABASE=hyperbola \
	-e MYSQL_USER=$(shell cd .. && dotenv get DB_USER | cut -d= -f 2) \
	-e MYSQL_PASSWORD=$(shell cd .. && dotenv get DB_PASSWORD | cut -d= -f 2)

.PHONY: migrate
migrate:
	docker run --network hyperbola -d -t hyperbola/app:latest /opt/manage.py migrate

.PHONY: fixtures
fixtures: DOCKER_OPTS := \
	-e AWS_ACCESS_KEY_ID=$(shell aws --profile default configure get aws_access_key_id) \
	-e AWS_SECRET_ACCESS_KEY=$(shell aws --profile default configure get aws_secret_access_key)

.PHONY: app
app: DOCKER_OPTS := \
	-e AWS_ACCESS_KEY_ID=$(shell aws --profile default configure get aws_access_key_id) \
	-e AWS_SECRET_ACCESS_KEY=$(shell aws --profile default configure get aws_secret_access_key) \
	-p 8009:8000

.PHONY: static
static: DOCKER_OPTS := \
	-p 8080:80 \
	-p 8888:8888

mysql fixtures app static:
	@env $$(if [[ "$@" == "mysql" ]]; then echo "HYP_SLEEP=10"; fi) HYP_DOCKER_OPTS="$(DOCKER_OPTS)" bin/launch-named-container $@-docker hyperbola/$@:latest

.PHONY: stop
stop:
	docker stop mysql-docker app-docker static-docker
