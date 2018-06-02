FROM python:3.6-alpine as config-build

ENV LC_ALL=C.UTF-8

RUN apk --no-cache add --virtual .hyperbola-build-deps \
        build-base python-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir ansible

COPY docker/backend/ansible /opt/ansible

ARG ansible_vault_password
ARG hyperbola_environment
RUN env $ansible_vault_password \
    ansible-playbook --connection=local --limit=localhost \
    -i localhost, \
    -e "ansible_python_interpreter=python3" \
    -e "hyperbola_environment=$hyperbola_environment" \
    --vault-id /opt/ansible/ansible_vault_password.py \
    /opt/ansible/backend.yml

FROM node as dist-build

COPY package.json yarn.lock webpack.config.js /opt/
COPY src /opt/src

RUN mkdir /opt/dist && \
    mkdir /opt/document-root && \
    cd /opt && \
    yarn install && \
    $(yarn bin)/webpack --mode production

FROM python:3.6-alpine as python-build

RUN apk --no-cache add --virtual .hyperbola-build-deps \
        build-base python-dev mariadb-dev jpeg-dev zlib-dev && \
    pip install --no-cache-dir pipenv

COPY hyperbola /opt/hyperbola
COPY docker/backend/settings.py /opt/hyperbola/
COPY MANIFEST.in Pipfile Pipfile.lock README.md setup.py setup.cfg /opt/

RUN cd /opt && \
    python -m venv venv && \
    venv/bin/pip install --no-cache-dir -U pip && \
    VIRTUAL_ENV=venv pipenv install && \
    env PBR_VERSION=0.134.0 \
        SKIP_GIT_SDIST=1 \
        SKIP_GENERATE_AUTHORS=1 \
        SKIP_WRITE_GIT_CHANGELOG=1 \
        venv/bin/python setup.py install

FROM python:3.6-alpine as python-backend
LABEL maintainer="Ryan Lopopolo <rjl@hyperbo.la>"

ENV LC_ALL=C.UTF-8

RUN apk --no-cache add --virtual .hyperbola-run-deps \
        mariadb-client-libs jpeg zlib

COPY --from=config-build /opt/.env /opt/.env
COPY --from=config-build /opt/gunicorn.py /opt/gunicorn.py
COPY --from=python-build /opt/venv /opt/venv
COPY manage.py /opt

RUN /opt/venv/bin/python /opt/manage.py minimizetemplates -m

COPY --from=dist-build /opt/document-root /opt/document-root
COPY --from=dist-build /opt/dist /opt/dist

RUN /opt/venv/bin/python /opt/manage.py collectstatic --no-input && \
    rm -rf /opt/dist

EXPOSE 8000

ENTRYPOINT ["/opt/venv/bin/python"]

CMD ["/opt/venv/bin/gunicorn", "--config", "/opt/gunicorn.py", "hyperbola.wsgi:application"]
