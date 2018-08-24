# Hyperbola Environment-Specific Configuration

This application attempts to emulate the [12 factor app](https://12factor.net/config)
and store config in the environment.

As part of packaging a deployment, configuration parameters may be written to
a `.env` file ([python-dotenv](https://github.com/theskumar/python-dotenv))
in the root of the repository.

The variables defined in the `.env` file get injected into the environment of
the python process.

All artifacts should contain a declaration of what type of deployment it is,
i.e.: production vs. local vs. dev.

The hyperbola deployment depends on the following environment variables being
present:

```
# provisioning
ANSIBLE_VAULT_PASSWORD='set-me'

ENVIRONMENT='production|local|stage|dev'
# venv/bin/python -c 'import django.core.management.utils as u; print(u.get_random_secret_key())'
SECRET_KEY='set-me'
DB_PASSWORD='set-me'
```

In the [local development](development.md) dev environment, you should also set
`ANSIBLE_VAULT_PASSWORD` to allow ansible to decrypt secrets during provisioning.
