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

1. Build Image
    ```bash
    make build-ami
    ```
2. Roll ASG
    ```bash
    pushd terraform/app-prod-pdx
    terraform plan
    terraform apply
    popd
    ```
3. Cleanup old AMIs
    ```bash
    bin/deregister_ami --dry-run
    bin/deregister_ami --execute
    ```

### Smoke Test

Verify that [frontpage](https://hyperbo.la/), [contact](https://hyperbo.la/contact/),
[lifestream](https://hyperbo.la/lifestream/), and [blog](https://hyperbo.la/w/) pages
function correctly.
