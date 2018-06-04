#!/usr/bin/env python
"""
Extract ansible vault password from the environment.

Used by docker image provisioning runs.
"""

import os
import sys


class AnsiblePasswordNotSetException(Exception):
    pass


def main():
    ansible_password = os.environ.get('ANSIBLE_VAULT_PASSWORD', None)
    if ansible_password is None:
        raise AnsiblePasswordNotSetException()
    return ansible_password


if __name__ == '__main__':
    try:
        print(main())
    except AnsiblePasswordNotSetException:
        print('ANSIBLE_VAULT_PASSWORD not set', file=sys.stderr)
        sys.exit(1)
