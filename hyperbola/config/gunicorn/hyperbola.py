import multiprocessing

bind = '127.0.0.1:7777'
workers = multiprocessing.cpu_count() + 1

pidfile = '/var/run/gunicorn_hyperbola.rjl.pid'
proc_name = 'live.hyperbo.la'

accesslog = '/hyperbola/var/log/gunicorn/hyperbola-live.access.log'
errorlog = '/hyperbola/var/log/gunicorn/hyperbola-live.error.log'
