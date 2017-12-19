# Release Process

## Local Dev

```bash
python -Wall manage.py runserver
```

### Smoke Test

Verify that [frontpage](http://127.0.0.1:8000/), [contact](http://127.0.0.1:8000/contact/), and
[lifestream](http://127.0.0.1:8000/lifestream/) pages function correctly.

## Cut Release Tag

```bash
make release
git push
git push --tags
```

## Deploy To Vagrant

```bash
vagrant up
vagrant provision
```

### Smoke Test

Verify that [frontpage](http://app-local.hyperboladc.net/), [contact](http://app-local.hyperboladc.net/contact/), and
[lifestream](http://app-local.hyperboladc.net/lifestream/) pages function correctly.

## AWS Deploy

```bash
# build image
make build-ami
# roll ASG
pushd terraform/env/app-prod-northwest
terraform plan
terraform apply
popd
# cleanup old AMIs
bin/deregister_ami --dry-run
bin/deregister_ami --execute
```
