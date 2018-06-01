GIT_REVISION := $(shell git rev-parse --short=12 HEAD)
GIT_DIRTY := $(shell git diff --no-ext-diff --quiet && \
	git diff --no-ext-diff --cached --quiet && \
	git ls-files --others --exclude-standard --directory --no-empty-directory --error-unmatch -- ':/*' >/dev/null 2>/dev/null || \
	echo ".dirty")
COMMITS_SINCE_TAG := $(shell git rev-list v0.134.0..HEAD --count)
HASH_LABEL := $(GIT_REVISION)$(GIT_DIRTY)
ifneq ($(COMMITS_SINCE_TAG)$(GIT_DIRTY), "0")
VERSION_LABEL := 0.134.0
else
VERSION_LABEL := dev
endif

.PHONY: all
all:

.PHONY: build
build: build-mysql build-app build-fixtures build-static build-ingress

.PHONY: build-mysql
build-mysql:
	docker build --pull -f mysql/Dockerfile -t hyperbola/mysql:$(HASH_LABEL) mysql

.PHONY: build-app
build-app:
	docker build \
		--build-arg hyperbola_environment=stage \
		--build-arg ansible_vault_password=$$(cd .. && dotenv get ANSIBLE_VAULT_PASSWORD) \
		--pull -f app/Dockerfile -t hyperbola/app:$(HASH_LABEL) ..
	docker tag hyperbola/app:$(HASH_LABEL) hyperbola/app:$(VERSION_LABEL)
	docker tag hyperbola/app:$(HASH_LABEL) hyperbola/app:latest

.PHONY: build-fixtures
build-fixtures:
	docker build -f fixtures/Dockerfile -t hyperbola/fixtures:$(HASH_LABEL) fixtures

.PHONY: build-static
build-static:
	docker pull nginx:stable-alpine
	docker build -f static/Dockerfile -t hyperbola/static:$(HASH_LABEL) ..
	docker tag hyperbola/static:$(HASH_LABEL) hyperbola/static:$(VERSION_LABEL)

.PHONY: build-ingress
build-ingress:
	docker build \
		--build-arg ansible_vault_password=$$(cd .. && dotenv get ANSIBLE_VAULT_PASSWORD) \
		--pull -f ingress/Dockerfile -t hyperbola/ingress:$(HASH_LABEL) ingress

.PHONY: dev
dev: mysql migrate fixtures app static ingress

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

.PHONY: static
.PHONY: ingress
ingress: DOCKER_OPTS := \
	-p 80:80 \
	-p 443:443

mysql fixtures app static ingress:
	@env $$(if [[ "$@" == "mysql" ]]; then echo "HYP_SLEEP=10"; fi) \
		HYP_DOCKER_OPTS="$(DOCKER_OPTS)" \
		bin/launch-named-container $@ hyperbola/$@:$(HASH_LABEL)

.PHONY: stop
stop:
	docker stop mysql app static ingress
