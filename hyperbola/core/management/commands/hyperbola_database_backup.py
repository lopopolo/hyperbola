#!/usr/bin/env python
"""
Back up django app data to S3.

The database is dumped using the django management command dumpdata.
The pretty-printed JSON file is uploaded to the S3 backup bucket.
"""

import datetime
import io
import tarfile
from pathlib import Path

import boto3
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Back up the results of the dumpdata command to S3"

    now = datetime.datetime.utcnow()
    S3_BACKUP_VERSION = getattr(settings, "HYPERBOLA_S3_BACKUP_VERSION", "v6")
    S3_BACKUP_TIMESTAMP = now.strftime("%Y-%m-%dT%H%MZ")
    S3_BACKUP_BUCKET = getattr(
        settings,
        "HYPERBOLA_S3_BACKUP_BUCKET",
        "hyperbola-app-backup-{}".format(settings.ENVIRONMENT),
    )
    S3_BACKUP_KEY_PREFIX = Path("{}/{}".format(S3_BACKUP_VERSION, settings.ENVIRONMENT))

    def handle(self, *args, **options):
        s3 = boto3.resource("s3", settings.AWS_REGION)

        dumpdata_file_name = "hyperbola-app-{}.json".format(self.S3_BACKUP_TIMESTAMP)
        dumpdata_archive_name = "{}.tar.gz".format(dumpdata_file_name)
        dumpdata_file_key = str(
            self.S3_BACKUP_KEY_PREFIX.joinpath("database", dumpdata_archive_name)
        )

        self.stdout.write("Preparing backup at {}".format(self.now.isoformat()))
        self.stdout.write(
            "Uploading backup to s3://{}/{}".format(self.S3_BACKUP_BUCKET, dumpdata_file_key)
        )
        with io.StringIO() as out, io.BytesIO() as outgz:
            call_command(
                "dumpdata",
                natural_foreign=True,
                indent=4,
                exclude=["sessions", "contenttypes", "auth.Permission"],
                stdout=out,
            )
            out_bytes = out.getvalue().encode("UTF-8")
            self.stdout.write("backup is {} bytes".format(len(out_bytes)))

            with tarfile.open(fileobj=outgz, mode="w:gz") as tar, io.BytesIO(out_bytes) as outbin:
                tarinfo = tarfile.TarInfo(name=dumpdata_file_name)
                tarinfo.size = len(out_bytes)
                tar.addfile(tarinfo=tarinfo, fileobj=outbin)

            s3.Bucket(self.S3_BACKUP_BUCKET).put_object(
                Key=dumpdata_file_key, Body=outgz.getvalue()
            )

        self.stdout.write(self.style.SUCCESS("Upload completed"))
