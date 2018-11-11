# hyperbo.la

This is the magic of <https://hyperbo.la>.

hyperbo.la is Ryan Lopopolo's personal website. Primary content consistes of a [blog](https://hyperbo.la/w/),
[contact page](https://hyperbo.la/contact/), and Twitter-like [lifestream](https://hyperbo.la/lifestream/).

hyperbo.la is built with [Django](https://www.djangoproject.com/). It can be [run locally](/doc/development.md)
via [Vagrant](/Vagrantfile) or deployed to AWS in a production configuration. It depends on [Ansible](/ansible),
[Packer](/packer), and [Terraform](/terraform) configuration in this repo.

## Dependencies

-   mysql
-   nginx
-   python3

## Build

Building a deployment of hyperbo.la happens self contained on the target host (Vagrant or AMI builder).
Build dependencies are [installed with Ansible](/ansible/roles/hyperbola-app/tasks/build-setup.yml).
Ansible also tries to [purge build dependencies](ansible/roles/hyperbola-app/tasks/build-cleanup.yml) from
the target host upon a successful deploy.

The python build is managed by [poetry](https://poetry.eustace.io/) and the static assets
build is managed by [webpack](https://webpack.js.org/).

## Deploy

To [deploy to AWS](/doc/release-process.md):

-   Cut a release
-   Build an AMI with packer
-   Perform a blue-green deployment with terraform
