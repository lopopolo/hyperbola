bind = 'unix:/hyperbola/var/sock/hyperbola-staging.sock'
workers = 1

accesslog = '/hyperbola/var/log/gunicorn/staging.access'
errorlog = '/hyperbola/var/log/gunicorn/staging.error'
loglevel = 'debug'
