#!/bin/sh

set -e

cd /hyperbola || exit 1

DB_HOST="mysql.app.hyperboladc.net"
DB_PORT="3306"
DB_USER="app"
DB_PASSWORD="$(eval "$(cat .env)" && echo "$DB_PASSWORD")"
DB_NAME="hyperbola"

mysql --host="$DB_HOST" --port="$DB_PORT" --user="$DB_USER" --password="$DB_PASSWORD" -e \
    "ALTER DATABASE $DB_NAME CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"

venv/bin/aws s3 cp \
    s3://hyperbola-app-backup-local/v5/local/database/hyperbola-app-2017-12-03T0126Z.json \
    hyperbola-fixtures.json

venv/bin/python manage.py loaddata hyperbola-fixtures.json
venv/bin/python manage.py createcachetable
