# Local Development

## External Dependencies

### MySQL

In a MySQL shell run:

```sql
create database hyperbola;
```

### pyenv

```bash
brew install pyenv pyenv-virtualenv
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
pyenv install "$(cat .python-version)"
```

### node + yarn

```bash
brew install node yarn
```


## Setup

```bash
git clone git@github.com:lopopolo/hyperbola.git
cd hyperbola
yarn install --ignore-engines
make virtualenv
bin/artifact-exec python -Wall app/manage.py migrate
bin/artifact-exec python -Wall app/manage.py createcachetable
```

## .env

To enable `artifact-exec` in dev, set `$PATH` in `env/00-path.env`:

```bash
export PATH="./venv/bin:$(yarn bin):$PATH"
```

Set the following parameters in `env/01-dev.env`:

```bash
export ENVIRONMENT="dev"
export SECRET_KEY=""

export DB_NAME="hyperbola"
export DB_USER="root"
export DB_PASSWORD=""
export DB_HOST="localhost"
export DB_PORT="3306"

export ANSIBLE_VAULT_PASSWORD=""
```

## runserver

```bash
bin/artifact-exec python -Wall app/manage.py runserver
```
