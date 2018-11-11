# Local Development

## External Dependencies

### MySQL

```bash
brew install mysql-connector-c
brew unlink mysql-connector-c
brew install mysql
```

### Vagrant

```bash
brew cask install vagrant
```

### Python

```bash
brew install pyenv
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
pyenv install "$(cat .python-version)"
pip install poetry
```

### Node

```bash
brew install node yarn
```

## Setup

```bash
git clone git@github.com:lopopolo/hyperbola.git
cd hyperbola
poetry install
poetry shell
inv init
vagrant up
```

## .env

In addition to the variables specified in [.env configuration](/doc/configuration.md),
you should also set `ANSIBLE_VAULT_PASSWORD` to allow ansible to decrypt secrets during
provisioning.
