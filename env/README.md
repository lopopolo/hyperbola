# Hyperbola Environment-Specific Configuration

This application attempts to emulate the [12 factor app](http://12factor.net/config)
and store config in the environment.

As part of packaging a deployment, configuration parameters may be written to
a set of shell scripts in this directory. Each script should be named like:

```
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
export ENVIRONMENT="production or staging or dev"
export SECRET_KEY="secret"

# database
export DB_NAME="mysql database"
export DB_USER="mysql username"
export DB_PASSWORD="mysql password"
export DB_HOST="name of database server"
export DB_PORT="port to connect to database server"

# debug
export DEBUG="true if in debug mode" # optional, defaults to false
```
