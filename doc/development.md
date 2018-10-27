# Local Development

## External Dependencies

### MySQL

```bash
brew install mysql@5.7
brew link mysql@5.7
```

### Vagrant

```bash
brew cask install vagrant
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

# Fill in from password vault
DB_PASSWORD=''

# Fill in from password vault
ANSIBLE_VAULT_PASSWORD=''
```
