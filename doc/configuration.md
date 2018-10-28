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

The hyperbola app depends on the following environment variables being
present:

| Env Variable | Value |
|-|-|
| ENVIRONMENT | One of: production, local, stage, dev |
| SECRET_KEY | Generate with `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` |
| DB_PASSWORD | Database password |
