#!/usr/bin/env python
"""
Back up django app data to S3.

The database is dumped using the django management command dumpdata.
The pretty-printed JSON file is uploaded to the S3 backup bucket.
"""

import datetime
import io
from pathlib import Path

import boto3
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Back up the results of the dumpdata command to S3'

    now = datetime.datetime.utcnow()
    S3_BACKUP_VERSION = getattr(settings, 'HYPERBOLA_S3_BACKUP_VERSION', 'v5')
    S3_BACKUP_TIMESTAMP = now.strftime('%Y-%m-%dT%H%MZ')
    S3_BACKUP_BUCKET = getattr(
        settings,
        'HYPERBOLA_S3_BACKUP_BUCKET',
        'hyperbola-app-backup-{}'.format(settings.ENVIRONMENT)
    )
    S3_BACKUP_KEY_PREFIX = Path('{}/{}'.format(S3_BACKUP_VERSION, settings.ENVIRONMENT))

    def handle(self, *args, **options):
        s3 = boto3.resource('s3', settings.AWS_REGION)

        dumpdata_file_name = 'hyperbola-app-{}.json'.format(self.S3_BACKUP_TIMESTAMP)
        dumpdata_file_key = str(self.S3_BACKUP_KEY_PREFIX.joinpath('database', dumpdata_file_name))

        self.stdout.write('Preparing backup at {}'.format(self.now.isoformat()))
        self.stdout.write('Uploading backup to s3://{}/{}'.format(self.S3_BACKUP_BUCKET, dumpdata_file_key))
        with io.StringIO() as out:
            call_command(
                'dumpdata',
                natural_foreign=True,
                indent=4,
                exclude=['sessions', 'contenttypes', 'auth.Permission'],
                stdout=out
            )
            s3.Bucket(self.S3_BACKUP_BUCKET).put_object(Key=dumpdata_file_key, Body=out.getvalue())

        self.stdout.write(self.style.SUCCESS('Upload completed'))
