# Ansible role to build Python

[![Build Status](https://travis-ci.org/torian/ansible-role-python.svg)](https://travis-ci.org/torian/ansible-role-python)

This ansible role will build python from source.

## Supported Platforms
  * EL / Centos (6 / 7)
  * Debian (Wheezy / Jessie)
  * Ubuntu (Trusty)
  * AMZ Linux

## Role Variables

The following role variables are defined in `defaults/main.yml`, and are the
ones required for you to be specified. The ones commented, are not defined.
For a detailed explanation about them you can take a look at the file.

```
#python_version: 2.7.11
#python_bin: /usr/local/bin/python2.7
#python_setuptools_bin: /usr/local/bin/easy_install-2.7

python_dev_packages: []
python_config_opts_default: '--with-ensurepip=install --enable-unicode=ucs4'
python_config_opts: ''

python_build_opts_default: '-j2 profile-opt'
python_build_opts: ''

python_force_build: False
setuptools_force_build: False
```

The variables that need to be specified, are:

  * `python_version`: Just that, 2.7.11, 3.5.1, or whatever version you need
  * `python_bin`: The path to the python binary that will be build, generally
    `/usr/local/bin/python<mayor.minor>`
  * `python_setuptools_bin`: The path to easy_install script to be build,
    generally `/usr/local/bin/easy-install-<mayor.minor>`

## Usage

To build the python interpreter you just need the following:

```
---
- hosts: some_host

  roles:
    - { 
        role: torian.python
        python_version: 2.7.11
        python_bin: /usr/local/bin/python2.7
        python_setuptools_bin: /usr/local/bin/easy-install-2.7
      }
```

The module can handle without issues building multiple python versions:

```
---
- hosts: some_host

  roles:
    - { 
        role: torian.python
        python_version: 2.7.11
        python_bin: /usr/local/bin/python2.7
        python_setuptools_bin: /usr/local/bin/easy-install-2.7
      }
    - { 
        role: torian.python
        python_version: 3.5.1
        python_bin: /usr/local/bin/python3.5
        python_setuptools_bin: /usr/local/bin/easy-install-3.5
      }
```

If yo need special configure or build parameters, and/or additional dev libs,
the following variables are available:

  * `python_dev_packages: []`
  * `python_config_opts: ''`
  * `python_build_opts: ''`

There are defaults for configure and build, that will be used in addition to the
above mentioned variables:

  * `python_config_opts_default: '--with-ensurepip=install --enable-unicode=ucs4'`
  * `python_build_opts_default: '-j2 profile-opt'`


## Distros with Python <= 2.7.9

Since the source code is downloaded from official python site, which forces
requests to `HTTPS`, if the distro's python version is lower than 2.7.9, support
for SNI might be missing, and you might see an error like:
```
msg: Failed to validate the SSL certificate for www.python.org:443. Make sure 
your managed systems have a valid CA certificate installed.  If the website 
serving the url uses SNI you need python >= 2.7.9 on your managed machine.  
You can use validate_certs=False if you do not need to confirm the server\s 
identity but this is unsafe and not recommended Paths checked for this 
platform: /etc/ssl/certs, /etc/pki/ca-trust/extracted/pem, /etc/pki/tls/certs,
/usr/share/ca-certificates/cacert.org, /etc/ansible
```

In that case, you need to set the following role var:

```
python_download_validate_certs: no
```

## License

See [License](LICENSE)

## Author Information

This role was created in 2016 by Emiliano Castagnari.

