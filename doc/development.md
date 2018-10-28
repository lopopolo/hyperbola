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

In addition to the variables specified in [.env configuration](/doc/configuration.md),
you should also set `ANSIBLE_VAULT_PASSWORD` to allow ansible to decrypt secrets during
provisioning.
