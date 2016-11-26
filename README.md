# hyperbola-tools

Build and deployment tools for https://hyperbo.la and https://wiki.hyperbo.la

## Local Development

Local development is done using Vagrant. Vagrant will provision a VM using
ansible.

## Note on `vagrant up` and `packer build`

`vagrant up` and `packer build` generate at least one certificate for the
image being built via ansible. Let's Encrypt has
[rate limits](https://letsencrypt.org/docs/rate-limits/) in place of 20
certificates per week per domain (*.hyperbo.la) and 5 duplicate certificates
per week. Keep this in mind when building from scratch.

Certificate counts for all domains can be found here:

- https://crt.sh/?q=wiki.hyperbo.la
- https://crt.sh/?q=wiki.local.hyperbo.la
- https://crt.sh/?q=hyperbo.la
- https://crt.sh/?q=staging.hyperbo.la

## Building Images with Ansible

Ansible + Vagrant + Packer can be used to build images for hyperbola-wiki.

### Goals

- No login deploys
- [x] wiki gems
- [ ] hyperbola app (production and local)
- No manual server configuration
- [ ] app: first five minutes
- [ ] app: app config
- [x] wiki: first five minutes
- [x] wiki: app config
- Let's Encrypt
- [x] Let's Encrypt bootstrapping
- [x] TLS in vagrant instances
