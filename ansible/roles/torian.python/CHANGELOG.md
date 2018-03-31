# Changelog

## 2017-10-09: 1.2.0

  - Python and PIP alternative priority (defaults to 50)
  - Removed build option `ensurepip` that installs pip with faulty entrypoints
  - Added back pip installation through setuptools

## 2017-10-05: 1.1.0
  
  - Add the ability to configure python and pip binaries as
    alternatives through the use of `python_alternative_enabled`
    and `python_pip_alternative_enabled` (default to false)

## 2017-10-03: 1.0.3
  
  - Update openssl package version fo AMZ Linux

## 2017-03-21: 1.0.2

  - Ansible lint - skip linting on some check commands

## 2017-03-17: 1.0.1

  - Ansible lint - Fixed trailing whitespace
  - Ansible lint - Use become instead of deprecated sudo

## 2016-10-06: 1.0.0
  
  - Toggle for certificates validation on source download
  - Travis integration

## 2016-05-14: 0.1.0

  - Initial commit

