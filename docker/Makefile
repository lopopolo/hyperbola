.PHONY: all
all:

.PHONY: build
build: build-prereq build-mysql build-backend build-fixtures build-static build-ingress

.PHONY: build-prereq
build-prereq:
	docker pull mysql:5.7
	docker pull python:3.6-alpine
	docker pull node
	docker pull nginx:stable-alpine

.PHONY: build-mysql
build-mysql:
	bin/build-hyperbola-image mysql stage

.PHONY: build-backend
build-backend:
	bin/build-hyperbola-image backend stage ..

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
stage: mysql migrate fixtures backend static ingress

.PHONY: mysql
mysql: DOCKER_OPTS := \
	-e "MYSQL_RANDOM_ROOT_PASSWORD=1" \
	-e "MYSQL_DATABASE=hyperbola" \
	-e "MYSQL_USER=app" \
	-e "MYSQL_PASSWORD=$$(eval "$$(cat ../.env)" && echo "$$DB_PASSWORD")"

.PHONY: migrate
migrate:
	docker run --network hyperbola -d -t hyperbola/backend:latest /opt/manage.py migrate

.PHONY: fixtures
fixtures: DOCKER_OPTS := \
	-e "AWS_ACCESS_KEY_ID=$$(aws --profile default configure get aws_access_key_id)" \
	-e "AWS_SECRET_ACCESS_KEY=$$(aws --profile default configure get aws_secret_access_key)"

.PHONY: backend
backend: DOCKER_OPTS := \
	-e "AWS_ACCESS_KEY_ID=$$(aws --profile default configure get aws_access_key_id)" \
	-e "AWS_SECRET_ACCESS_KEY=$$(aws --profile default configure get aws_secret_access_key)" \

.PHONY: static
.PHONY: ingress
ingress: DOCKER_OPTS := \
	-p 80:80 \
	-p 443:443

mysql fixtures backend static ingress:
	HYP_DOCKER_OPTS="$(DOCKER_OPTS)" bin/launch-named-container $@.app.hyperboladc.net hyperbola/$@:stage

.PHONY: stop
stop:
	docker stop mysql.app.hyperboladc.net \
		backend.app.hyperboladc.net \
		static.app.hyperboladc.net \
		ingress.app.hyperboladc.net
