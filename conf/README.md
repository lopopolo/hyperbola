# nginx configuration

Inspired by [HTML5 Boilerplate](https://github.com/h5bp/server-configs-nginx).

Symlink the sites in the root of this directory into `/etc/nginx/sites-enabled`.

All access logs and all error logs are piped to the same place across all sites.

In each server block, include all directives by including `directives/*.conf`.
