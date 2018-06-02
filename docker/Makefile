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
build: build-prereq build-mysql build-app build-fixtures build-static build-ingress

.PHONY: build-prereq
build-prereq:
	docker pull mysql:5.7
	docker pull python:3.6-alpine
	docker pull node
	docker pull nginx:stable-alpine

.PHONY: build-mysql
build-mysql:
	bin/build-hyperbola-image mysql stage

.PHONY: build-app
build-app:
	bin/build-hyperbola-image app stage ..

.PHONY: build-fixtures
build-fixtures:
	bin/build-hyperbola-image fixtures stage

.PHONY: build-static
build-static:
	bin/build-hyperbola-image static stage

.PHONY: build-ingress
build-ingress:
	bin/build-hyperbola-image ingress stage

.PHONY: stage
stage: mysql migrate fixtures app static ingress

.PHONY: mysql
mysql: DOCKER_OPTS := \
	-e "MYSQL_RANDOM_ROOT_PASSWORD=1" \
	-e "MYSQL_DATABASE=hyperbola" \
	-e "MYSQL_USER=app" \
	-e "MYSQL_PASSWORD=$$(env "$$(dotenv -f ../.env get DB_PASSWORD)" printenv DB_PASSWORD)"

.PHONY: migrate
migrate:
	docker run --network hyperbola -d -t hyperbola/app:latest /opt/manage.py migrate

.PHONY: fixtures
fixtures: DOCKER_OPTS := \
	-e "AWS_ACCESS_KEY_ID=$$(aws --profile default configure get aws_access_key_id)" \
	-e "AWS_SECRET_ACCESS_KEY=$$(aws --profile default configure get aws_secret_access_key)"

.PHONY: app
app: DOCKER_OPTS := \
	-e "AWS_ACCESS_KEY_ID=$$(aws --profile default configure get aws_access_key_id)" \
	-e "AWS_SECRET_ACCESS_KEY=$$(aws --profile default configure get aws_secret_access_key)" \

.PHONY: static
.PHONY: ingress
ingress: DOCKER_OPTS := \
	-p 80:80 \
	-p 443:443

mysql fixtures app static ingress:
	HYP_DOCKER_OPTS="$(DOCKER_OPTS)" bin/launch-named-container $@ hyperbola/$@:stage

.PHONY: stop
stop:
	docker stop mysql app static ingress
