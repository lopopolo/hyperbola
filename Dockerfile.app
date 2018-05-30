FROM ubuntu:18.04 as app-vm
MAINTAINER Ryan Lopopolo <rjl@hyperbo.la>

ENV LC_ALL=C.UTF-8

RUN apt-get update && \
    apt-get -y install software-properties-common && \
    apt-add-repository -y ppa:ansible/ansible && \
    apt-get update && \
    apt-get -y install ansible python-pip

COPY bin /opt/bin
COPY ansible /opt/ansible

ARG ansible_vault_password
RUN env $ansible_vault_password printenv ANSIBLE_VAULT_PASSWORD > /tmp/vault-password.txt

RUN ansible-playbook --connection=local -i localhost, /opt/ansible/provision.yml
RUN ansible-playbook --connection=local --limit=localhost -i /opt/ansible/local.ini --extra-vars "hyperbola_driver=docker" --vault-password-file=/tmp/vault-password.txt /opt/ansible/app.yml

FROM python:3.6-alpine as python-build
MAINTAINER Ryan Lopopolo <rjl@hyperbo.la>

COPY hyperbola /opt/hyperbola
COPY MANIFEST.in /opt
COPY Pipfile /opt
COPY Pipfile.lock /opt
COPY README.md /opt
COPY setup.py /opt
COPY setup.cfg /opt
COPY --from=app-vm /hyperbola/app/current/.env /opt/.env

RUN apk --no-cache add --virtual .hyperbola-build-deps \
        build-base python-dev mariadb-dev jpeg-dev zlib-dev && \
    pip install --no-cache-dir pipenv pex

#RUN pex --help && exit 1

RUN cd /opt && \
    python -m venv venv && \
    venv/bin/pip install --no-cache-dir -U pip && \
    VIRTUAL_ENV=venv pipenv install && \
    env PBR_VERSION=0.134.0 \
        SKIP_GIT_SDIST=1 \
        SKIP_GENERATE_AUTHORS=1 \
        SKIP_WRITE_GIT_CHANGELOG=1 \
        venv/bin/python setup.py install

FROM python:3.6-alpine as python-app

COPY --from=python-build /opt/venv /opt/venv
COPY --from=python-build /opt/.env /opt/.env

RUN apk --no-cache add --virtual .hyperbola-run-deps \
        mariadb-client-libs jpeg zlib

EXPOSE 8000

ENTRYPOINT ["/opt/venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "hyperbola.wsgi:application"]

# vim:set ft=dockerfile:
