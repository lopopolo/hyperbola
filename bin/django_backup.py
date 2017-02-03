#!/usr/bin/env python

import contextlib
import datetime
import os
import shutil
import smtplib
import tarfile
import tempfile
from email.encoders import encode_base64
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

import django
from django.conf import settings
from django.core.management import call_command


def send_mail(send_from, send_to, subject, text='', files=None, server='smtp.gmail.com:587', credentials=('', '')):
    files = files or []
    assert type(send_to) == list
    assert type(files) == list
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    for attachment_path in files:
        part = MIMEBase('application', 'octet-stream')
        with open(attachment_path, 'rb') as attachment:
            part.set_payload(attachment.read())
        encode_base64(part)
        part.add_header(
            'Content-Disposition',
            'attachment; filename="{0}"'.format(os.path.basename(attachment_path)))
        msg.attach(part)
    smtp = smtplib.SMTP(server)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(*credentials)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


def make_tarfile(output_filename, source_dir, tarfilter=None):
    with tarfile.open(output_filename, 'w:gz', dereference=True) as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir), filter=tarfilter)


@contextlib.contextmanager
def tempdir():
    """A context manager for creating and removing temporary directories."""
    temp = tempfile.mkdtemp()
    try:
        yield temp
    finally:
        shutil.rmtree(temp)


if __name__ == '__main__':
    backup_time = datetime.datetime.now().strftime('%Y-%m-%dT%H%M')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hyperbola.settings')
    django.setup()

    email_creds = (settings.BACKUP_EMAIL_LOGIN_USERNAME, settings.BACKUP_EMAIL_LOGIN_PASSWORD)

    with tempdir() as temp_dir:
        # Backup all models
        datadumpfile = '{0}/hyperbola-app-{1}.json'.format(temp_dir, backup_time)
        with open(datadumpfile, 'w') as f:
            call_command(
                'dumpdata',
                natural_foreign=True,
                indent=4,
                exclude=['sessions', 'contenttypes', 'auth.Permission'],
                stdout=f
            )

        send_mail(
            send_from='rjl@hyperbo.la',
            send_to=['upload.databas.skvvczqkcv@u.box.com'],
            subject='hyperbo.la cron django datadump',
            files=[datadumpfile],
            credentials=email_creds,
        )

        # Backup all django media from hyperbola.settings.MEDIA_ROOT
        def prune_cache_from_media(tarinfo):
            if tarinfo.name.startswith("{}/cache".format(settings.ENVIRONMENT.environment.value)):
                return None
            return tarinfo

        media_tar_file = '{0}/{1}.media.tar.gz'.format(temp_dir, backup_time)
        make_tarfile(media_tar_file, settings.MEDIA_ROOT, prune_cache_from_media)

        send_mail(
            send_from='rjl@hyperbo.la',
            send_to=['upload.media.palovsbp7s@u.box.com'],
            subject='hyperbo.la cron media backup',
            files=[media_tar_file],
            credentials=email_creds,
        )
