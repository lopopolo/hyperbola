bind = 'unix:/hyperbola/var/sock/hyperbola-staging.sock'
workers = 1

pidfile = '/var/run/gunicorn/staging.pid'

accesslog = '/hyperbola/var/log/gunicorn/staging.access'
errorlog = '/hyperbola/var/log/gunicorn/staging.error'
