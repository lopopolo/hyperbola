# Local Development

## External Dependencies

### MySQL

In a MySQL shell run:

```sql
create database hyperbola;
```

### pyenv + pyenv-virtualenv

```bash
brew install pyenv pyenv-virtualenv
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
pyenv install "$(cat .python-version)"
```

### node + yarn

```bash
brew install node@6
cd bin
wget https://yarnpkg.com/latest.tar.gz
tar xzf latest.tar.gz
echo '*' > dist/.gitignore
rm latest.tar.gz
```


## Setup

```bash
git clone git@github.com:lopopolo/hyperbola.git
# make local media directory
mkdir media/dev
make virtualenv
bin/artifact-exec python -Wall app/manage.py migrate
```

## .env

To enable `artifact-exec` in dev, set `$PATH` in `env/00-path.env`:

```bash
export PATH="./bin/dist/bin:/usr/local/opt/node@6/bin:$PATH"
export PATH="./virtualenv/bin:$(npm bin):$PATH"
```

Set the following parameters in `env/01-dev.env`:

```bash
export ENVIRONMENT="dev"
export SECRET_KEY="$(uuidgen)"

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
