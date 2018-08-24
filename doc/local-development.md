# Local Development

## External Dependencies

### MySQL

Install MySQL:

```bash
brew install mysql@5.7
brew link mysql@5.7
```

In a MySQL shell run:

```sql
create database hyperbola;
```

### pyenv

```bash
brew install pyenv
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
yarn install
make virtualenv
source venv/bin/activate
vagrant up
```

## .env

To configure hyperbola for dev, set the following parameters in `.env`:

```
ENVIRONMENT='dev'
# Generate with:
# $ python -c 'import django.core.management.utils; print(django.core.management.utils.get_random_secret_key())'
SECRET_KEY=''

DB_HOST='127.0.0.1'
DB_PORT='13306'
DB_USER='app'
DB_NAME='hyperbola'
# Fill in from password vault
DB_PASSWORD=''

# Fill in from password vault
ANSIBLE_VAULT_PASSWORD=''
```

## runserver

```bash
python -Wall manage.py runserver
```
