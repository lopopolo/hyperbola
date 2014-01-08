#!/usr/bin/env ruby

BACKUP_TIME = Time.now.strftime("%Y-%m-%d %Hh%Mm")

SITE_ROOT = File.dirname(File.dirname(__FILE__))
BACKUP_DIR = "/hyperbola/backups"
MEDIA_DIR = "/hyperbola/media"

%x[mysqldump --defaults-extra-file=#{SITE_ROOT}/hyperbola/db.cnf --all-databases 2>/dev/null 1> "#{BACKUP_DIR}/#{BACKUP_TIME}.mysql.sql"]

%x[tar -C #{MEDIA_DIR} -zcf "#{BACKUP_DIR}/#{BACKUP_TIME}.media.tar.gz" .]

