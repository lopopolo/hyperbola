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

FROM python:3 as python-base
MAINTAINER Ryan Lopopolo <rjl@hyperbo.la>

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install -U setuptools pipenv && \
    pipenv install --system --deploy && \
    rm -rf /root/.cache Pipfile Pipfile.lock

COPY hyperbola /opt/hyperbola
COPY MANIFEST.in /opt
COPY README.md /opt
COPY setup.py /opt
COPY setup.cfg /opt
COPY --from=app-vm /hyperbola/app/current/.env /opt/.env

RUN cd /opt && \
    env PBR_VERSION=0.134.0 \
        SKIP_GIT_SDIST=1 \
        SKIP_GENERATE_AUTHORS=1 \
        SKIP_WRITE_GIT_CHANGELOG=1 \
        python setup.py install

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "hyperbola.wsgi:application"]
