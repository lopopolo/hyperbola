import multiprocessing

bind = 'unix:/hyperbola/var/sock/hyperbola-production.sock'
workers = multiprocessing.cpu_count() + 1

pidfile = '/var/run/gunicorn/production.pid'

accesslog = '/hyperbola/var/log/gunicorn/production.access'
errorlog = '/hyperbola/var/log/gunicorn/production.error'
