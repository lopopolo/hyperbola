#!/usr/bin/env python

# Backup hyperbo.la database and media directories to
# Box via email folder upload.
#
# adapted from: http://stackoverflow.com/a/3363254

import contextlib
import datetime
import os
import shutil
import smtplib
import subprocess
import tarfile
import tempfile
from email.encoders import encode_base64
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def source(env):
    prop = os.environ.get(env)
    if not prop:
        raise Exception('Environment variable {0} not set'.format(env))

    if prop in ['yes', 'true']:
        return True
    elif prop in ['no', 'false']:
        return False
    else:
        return prop


def send_mail(
        send_from, send_to,
        subject, text,
        files=None, server='localhost'):
    files = files or []

    assert type(send_to) == list
    assert type(files) == list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files:
        part = MIMEBase('application', 'octet-stream')
        with open(f, 'rb') as attachment:
            part.set_payload(attachment.read())
        encode_base64(part)
        part.add_header(
            'Content-Disposition',
            'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, 'w:gz') as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


@contextlib.contextmanager
def tempdir():
    """A context manager for creating and removing temporary directories"""
    temp = tempfile.mkdtemp()
    try:
        yield temp
    finally:
        shutil.rmtree(temp)


if __name__ == '__main__':
    backup_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')

    with tempdir() as temp_dir:
        # Backup all databases and tables in MySQL
        mysql_dump_file = '{0}/{1}.mysql.sql'.format(temp_dir, backup_time)
        mysqldump_command = [
            'mysqldump',
            '--user={0}'.format(source('DB_USER')),
            '--password={0}'.format(source('DB_PASSWORD')),
            '--host={0}'.format(source('DB_HOST')),
            '--port={0}'.format(source('DB_PORT')),
            '--all-databases'
        ]

        with open(mysql_dump_file, 'w') as mysqlf:
            with open(os.devnull, 'w') as FNULL:
                subprocess.call(mysqldump_command, stdout=mysqlf, stderr=FNULL)

        send_mail(
            send_from='rjl@hyperbo.la',
            send_to=['upload.databas.skvvczqkcv@u.box.com'],
            subject='hyperbo.la cron mysqldump',
            text='',
            files=[mysql_dump_file]
        )

        # Backup all django media from hyperbola.settings.MEDIA_ROOT
        media_root = '/hyperbola/media'
        media_tar_file = '{0}/{1}.media.tar.gz'.format(temp_dir, backup_time)
        make_tarfile(media_tar_file, media_root)

        send_mail(
            send_from='rjl@hyperbo.la',
            send_to=['upload.media.palovsbp7s@u.box.com'],
            subject='hyperbo.la cron media backup',
            text='',
            files=[media_tar_file]
        )
