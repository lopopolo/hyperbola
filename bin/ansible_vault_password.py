#!/usr/bin/env python
"""
Extract ansible vault password from dotenv.

Used by Vagrant and Packer provisioning runs.
"""

import os
import sys

from dotenv import find_dotenv, load_dotenv


class AnsiblePasswordNotSetException(Exception):
    pass


def main():
    load_dotenv(find_dotenv())
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
