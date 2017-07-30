# Hyperbola Environment-Specific Configuration

This application attempts to emulate the [12 factor app](http://12factor.net/config)
and store config in the environment.

As part of packaging a deployment, configuration parameters may be written to
a set of shell scripts in this directory. Each script should be named like:

```
00-path.env
01-environment.env
02-database.env
# ...
```

All `*.env` files will be sourced in order as part of starting the application
server.

All artifacts should contain a declaration of what type of deployment it is,
i.e.: production vs. staging vs. development.

The hyperbola deployment depends on the following environment variables being
present:

```sh
# environment
export ENVIRONMENT="production|staging|local|dev"
# venv/bin/python -c 'import django.core.management.utils as u; print(u.get_random_secret_key())'
export SECRET_KEY=""

# database
export DB_HOST='127.0.0.1'
export DB_PORT='3306'
export DB_USER='root'
export DB_PASSWORD=''
export DB_NAME='hyperbola'

# cache
export REDIS_HOST='redis.local.hyperboladc.net'
export REDIS_PORT='6379'
export REDIS_PASSWORD=''
export REDIS_NAME='0'

# debug
export DEBUG='false' # optional, defaults to false

# deploy and provisioning
export ANSIBLE_VAULT_PASSWORD=''
```
