# Local Development

## External Dependencies

- MySQL
- Redis

In a MySQL shell run:

```
create database hyperbola;
```

## Setup

```bash
git clone git@github.com:lopopolo/hyperbola.git
# make local media directory
mkdir media/dev
make wipe-virtualenv
make virtualenv
bin/artifact-exec python -Wall app/manage.py migrate
```

## .env

To enable `artifact-exec` in dev, set `$PATH` in `env/00-path.env`:

```bash
export PATH="./virtualenv/bin:$(npm bin):$PATH"
```

Set the following parameters in `env/01-dev.env`:

```bash
export ENVIRONMENT="dev"
export SECRET_KEY="$(uuidgen)"

export DB_NAME="hyperbola"
export DB_NAME="hyperbola"
export DB_USER="root"
export DB_PASSWORD=""
export DB_HOST="localhost"
export DB_PORT="3306"
```

## runserver

```bash
bin/artifact-exec python -Wall app/manage.py runserver
```
