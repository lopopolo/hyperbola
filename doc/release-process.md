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
inv release
```

## Deploy To AWS

The `deploy` task performs the following actions:

-   Build an AMI using Packer.
-   Update launch template to use new AMI with Terraform.
-   Cycle the backend ASG to pick up the new AMI.

```bash
inv deploy
```

### Smoke Test

Verify that [frontpage](https://hyperbo.la/), [contact](https://hyperbo.la/contact/),
[lifestream](https://hyperbo.la/lifestream/), and [blog](https://hyperbo.la/w/) pages
function correctly.

### Rollback a Bad Deploy

The `deploy.rollback` task performs the following actions:

-   Revert the HEAD commit (assumed to be a version bump commit).
-   Update launch template to use new AMI with Terraform.
-   Cycle the backend ASG to pick up the old AMI.

```bash
inv deploy.rollback
```

### Cleanup

The `deploy.finalize` task performs the following actions:

-   Delete unused AMIs.
-   Delete unused snapshots.

```bash
inv deploy.finalize
```
