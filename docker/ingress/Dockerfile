FROM python:3.6-alpine as cert-build

ENV LC_ALL=C.UTF-8

RUN apk --no-cache add --virtual .hyperbola-build-deps \
        build-base python-dev libffi-dev openssl openssl-dev && \
    pip install --no-cache-dir ansible boto pyopenssl

RUN mkdir -p /etc/ssl && \
    openssl genrsa -des3 -passout pass:x -out /etc/ssl/key.pem 2048 && \
    openssl rsa -passin pass:x -in /etc/ssl/key.pem -out /etc/ssl/snakeoil.key && \
    openssl req -new -key /etc/ssl/snakeoil.key -out /etc/ssl/cert.csr -subj "/C=US/ST=CA/L=San Francisco/O=Ryan Lopopolo/OU=hyperbola/CN=default" && \
    openssl x509 -req -days 3650 -in /etc/ssl/cert.csr -signkey /etc/ssl/snakeoil.key -out /etc/ssl/snakeoil.pem

COPY ansible /opt/ansible

ARG ansible_vault_password
ARG hyperbola_environment
RUN env $ansible_vault_password \
    ansible-playbook --connection=local --limit=localhost \
    -i localhost, \
    -e "ansible_python_interpreter=python3" \
    -e "hyperbola_environment=$hyperbola_environment" \
    --vault-id /opt/ansible/ansible_vault_password.py \
    /opt/ansible/ingress.yml

FROM nginx:stable-alpine
LABEL maintainer="Ryan Lopopolo <rjl@hyperbo.la>"

RUN rm /etc/nginx/conf.d/default.conf

COPY ingress.conf /etc/nginx/conf.d/ingress.conf
COPY ssl.conf ssl-stapling.conf /etc/nginx/conf.d/ssl/
COPY --from=cert-build /etc/ssl/snakeoil.key /etc/ssl/snakeoil.pem /etc/ssl/
COPY --from=cert-build /etc/ssl/stage.hyperboladc.net/stage.hyperboladc.net.key /etc/ssl/
COPY --from=cert-build /etc/ssl/stage.hyperboladc.net/stage.hyperboladc.net.pem /etc/ssl/

EXPOSE 80
EXPOSE 443
