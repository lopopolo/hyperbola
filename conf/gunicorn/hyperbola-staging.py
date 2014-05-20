bind = 'unix:/hyperbola/var/sock/hyperbola-staging.sock'
workers = 1

pidfile = '/var/run/gunicorn_hyperbola-staging.rjl.pid'
proc_name = 'staging.hyperbo.la'

accesslog = '/hyperbola/var/log/gunicorn/hyperbola-staging.access.log'
errorlog = '/hyperbola/var/log/gunicorn/hyperbola-staging.error.log'
loglevel = 'debug'
