#!/bin/sh

set -e

cd /opt || exit 1

DB_HOST="$(venv/bin/dotenv get DB_HOST | cut -d= -f 2)"
DB_PORT="$(venv/bin/dotenv get DB_PORT | cut -d= -f 2)"
DB_USER="$(venv/bin/dotenv get DB_USER | cut -d= -f 2)"
DB_PASSWORD="$(venv/bin/dotenv get DB_PASSWORD | cut -d= -f 2)"
DB_NAME="$(venv/bin/dotenv get DB_NAME | cut -d= -f 2)"

mysql --host="$DB_HOST" --port="$DB_PORT" --user="$DB_USER" --password="$DB_PASSWORD" -e \
    "ALTER DATABASE $DB_NAME CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"

venv/bin/aws s3 cp \
    s3://hyperbola-app-backup-local/v5/local/database/hyperbola-app-2017-12-03T0126Z.json \
    hyperbola-fixtures.json

venv/bin/python manage.py loaddata hyperbola-fixtures.json
venv/bin/python manage.py createcachetable
