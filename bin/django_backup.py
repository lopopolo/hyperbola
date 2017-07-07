#!/usr/bin/env python
"""
Back up django app data to S3.

The database is dumped using the django management command dumpdata.
The pretty-printed JSON file is uploaded to the S3 backup bucket.
"""

import datetime
import io
import os
from pathlib import Path

import boto3
import django
from django.conf import settings
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hyperbola.settings')
django.setup()

BACKUP_VERSION = 'v5'
BACKUP_TIMESTAMP = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H%MZ')
S3_BUCKET = 'hyperbola-app-backup'
S3_KEY_PREFIX = Path('{}/{}'.format(BACKUP_VERSION, settings.ENVIRONMENT))


if __name__ == '__main__':
    s3 = boto3.resource('s3')
    # Backup all models
    dumpdata_file_name = 'hyperbola-app-{0}.json'.format(BACKUP_TIMESTAMP)
    dumpdata_file_key = str(S3_KEY_PREFIX.joinpath('database', dumpdata_file_name))
    with io.StringIO() as out:
        call_command(
            'dumpdata',
            natural_foreign=True,
            indent=4,
            exclude=['sessions', 'contenttypes', 'auth.Permission'],
            stdout=out
        )
        s3.Bucket(S3_BUCKET).put_object(Key=dumpdata_file_key, Body=out.getvalue())
