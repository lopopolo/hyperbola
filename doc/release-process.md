# Release Process

## Smoke Test

```bash
bin/artifact-exec python manage.py runserver
```

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
make tunnel
bin/artifact-exec vagrant provision
```

### Smoke Test

Verify that [frontpage](http://app-local.hyperboladc.net/), [contact](http://app-local.hyperboladc.net/contact/), and
[lifestream](http://app-local.hyperboladc.net/lifestream/) pages function correctly.

## AWS Deploy

```
# build image
bin/artifact-exec packer build packer/app.json
# roll ASG
pushd terraform/env/app-prod-northwest
terraform plan
terraform apply
popd
# cleanup old AMIs
bin/artifact-exec deregister_ami --dry-run
bin/artifact-exec deregister_ami --execute
```
