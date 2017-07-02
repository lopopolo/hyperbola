# wiki role vars

## deploy-keys.yml

Encrypted with ansible-vault.

```yaml
wiki_ssh_deploy_key: "rsa private key for deploy key attached to wiki repo"
```

## htpasswd.yml

Encrypted with ansible-vault.

```yaml
# list of users and passwords to give access to wiki
wiki_htpasswd:
  users:
  - username: "user"
    password: "password"
```
