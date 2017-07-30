# hyperbo.la

This is the magic of <https://hyperbo.la>.

hyperbo.la is a django website. It can be [run locally](/doc/local-development.md)
or deployed in production and staging configurations. It depends on [Ansible](/ansible),
[Packer](/packer), and [Terraform](/terraform) configuration in this repo.

## Dependencies

### Run

* mysql
* nginx
* python3 ~= 3.5.3
* redis ~= 3.2.4

### Build

* make
* nodejs
* yarn

# hyperbola-tools

Build and deployment tools for <https://hyperbo.la> and <https://wiki.hyperbo.la>

## Dependencies

### Build

* ansible
* make
* packer
* vagrant

### Deploy

* AWS
* CloudFlare
* terraform

## Local Development

Local development is done using Vagrant. Vagrant will provision a VM using
ansible.

## Building Images with Ansible

Ansible + Vagrant + Packer can be used to build images for hyperbola-wiki.
