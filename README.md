# hyperbo.la

This is the magic of https://hyperbo.la.

hyperbo.la is a django website. It can be [run locally](LOCAL-DEVELOPMENT.md)
or deployed in production and staging configurations. It depends on configuration
found in [hyperbola-tools](https://github.com/lopopolo/hyperbola-tools).

## Dependencies

* python3 ~= 3.5.3
* mysql
* nginx
* nodejs >= 6.9 LTS
* redis ~= 3.2.4

# hyperbola-tools

Build and deployment tools for https://hyperbo.la and https://wiki.hyperbo.la

## Local Development

Local development is done using Vagrant. Vagrant will provision a VM using
ansible.

## Building Images with Ansible

Ansible + Vagrant + Packer can be used to build images for hyperbola-wiki.
