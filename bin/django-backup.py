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
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders


def send_mail(send_from, send_to, subject, text, files=[], server="localhost"):
    assert type(send_to) == list
    assert type(files) == list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files:
        part = MIMEBase('application', "octet-stream")
        with open(f, "rb") as attachment:
            part.set_payload(attachment.read())
        Encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


@contextlib.contextmanager
def tempdir():
    """A context manager for creating and removing temporary directories"""
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)


site_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
backup_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")

with tempdir() as temp_dir:
    # Backup all databases and tables in MySQL
    mysql_dump_file = "{0}/{1}.mysql.sql".format(temp_dir, backup_time)

    with open(mysql_dump_file, "w") as mysqlf:
        with open(os.devnull, 'w') as FNULL:
            subprocess.call(
                ["mysqldump",
                 "--defaults-extra-file={0}/hyperbola/db.cnf".format(site_root),
                 "--all-databases"],
                stdout=mysqlf,
                stderr=FNULL
            )

    send_mail("rjl@hyperbo.la", ["upload.databas.skvvczqkcv@u.box.com"],
              "hyperbo.la cron mysqldump", "", [mysql_dump_file])

    # Backup all django media from hyperbola.settings.MEDIA_ROOT
    media_root = "/hyperbola/media"
    media_tar_file = "{0}/{1}.media.tar.gz".format(temp_dir, backup_time)
    make_tarfile(media_tar_file, media_root)

    send_mail("rjl@hyperbo.la", ["upload.media.palovsbp7s@u.box.com"],
              "hyperbo.la cron media backup", "", [media_tar_file])
