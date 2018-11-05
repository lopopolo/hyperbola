# Release Process

## Deploy To Vagrant

```bash
vagrant up
vagrant provision
```

### Smoke Test

Verify that [frontpage](https://local.hyperboladc.net/), [contact](https://local.hyperboladc.net/contact/),
[lifestream](https://local.hyperboladc.net/lifestream/), and [blog](https://local.hyperboladc.net/w/)
pages function correctly.

## Cut Release Tag

```bash
make release
git push
git push --tags
```

## Deploy To AWS

```bash
make build-ami # build image
pushd terraform/app-prod-pdx
terraform plan
terraform apply # update launch template
popd
bin/cycle-asg # launch new instances with the new image
# smoke test
bin/deregister_ami --dry-run
bin/deregister_ami --execute # cleanup old images
```

### Smoke Test

Verify that [frontpage](https://hyperbo.la/), [contact](https://hyperbo.la/contact/),
[lifestream](https://hyperbo.la/lifestream/), and [blog](https://hyperbo.la/w/) pages
function correctly.

### Rollback a Bad Deploy

```bash
git revert
pushd terraform/app-prod-pdx
terraform plan
terraform apply # update launch template
popd
bin/cycle-asg # launch new instances with the old image
```
