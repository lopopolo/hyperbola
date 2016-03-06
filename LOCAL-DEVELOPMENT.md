# Local Development

## External Dependencies

- MySQL
- Redis

In a MySQL shell run:

```
create database hyperbola;
```

## Setup

```
git clone git@github.com:lopopolo/hyperbola.git
# make local media directory
mkdir dev-media
echo '*' > dev-media/.gitignore
# make virtualenv
virtualenv virtualenv
virtualenv/bin/pip install -r dev-requirements.txt --ignore-installed
```

## .env

Set the following parameters in `env/01-dev.env`:

```
export ENVIRONMENT="dev"
export SECRET_KEY="notarealsecretdeadbeefdeadbeef"

export DB_NAME="hyperbola"
export DB_USER="root"
export DB_PASSWORD=""
export DB_HOST="localhost"
export DB_PORT="3306"
```

## runserver

```
virtualenv/bin/python -Wall app/manage.py runserver
```

# Known Issues

- The contact-resume-pdf route does not work due to its dependence on `X-Accel-Redirect`
  and nginx. nginx is not present in dev.
