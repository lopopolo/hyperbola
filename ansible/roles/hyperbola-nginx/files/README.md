# nginx configuration

Inspired by [HTML5 Boilerplate's nginx configs](https://github.com/h5bp/server-configs-nginx).

Copy the sites in `sites` into `/etc/nginx/sites-enabled`. `00-no-default.nginx.conf` is the
default site for HTTP and HTTPS. It returns no content. The HTTPS listener uses the snakeoil
certs. The default site conf file includes listener options for port binding and includes http-
level configs from `conf.d/nginx-base-config/base/*.conf`.

`nginx-base-config` contains common configs for all sites deployed on hyperbo.la:

* asset caching
* health checks
* security headers
* SSL configuration

When deploying a new site, include all `location` and `directive-only` configs by adding the
following lines to the end of the server block:

```nginx
server {
    location / {
        try_files $uri @upstream;

        include conf.d/nginx-base-config/location/*.conf;
    }

    location /static {
        alias /hyperbola/static/;
        include /hyperbola/tools/nginx/location/static/*.conf;
        include /hyperbola/tools/nginx/directive-only/static/*.conf;
    }

    include conf.d/nginx-base-config/directive-only/*.conf;
}
```

SSL configs in `directive-only/ssl` should be `include`d individually.
