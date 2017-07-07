# nginx configuration

Inspired by [HTML5 Boilerplate's nginx configs](https://github.com/h5bp/server-configs-nginx).

Symlink the sites in `sites` into `/etc/nginx/sites-enabled`.

This site contains common configs for all sites deployed on hyperbo.la:

* asset caching
* security headers
* SSL configuration

When deploying a new site, include all `location` and `directive-only`
configs by adding the following lines to the end of the server block:

```nginx
server {
    // snip ...

    include /hyperbola/tools/nginx/location/*.conf;
    include /hyperbola/tools/nginx/directive-only/*.conf;
}
```

SSL configs in `ssl-directive-only` should be `include`d individually.
