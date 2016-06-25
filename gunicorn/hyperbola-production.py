import multiprocessing

bind = 'unix:/tmp/hyperbola-production.sock'
workers = multiprocessing.cpu_count() + 1
daemon = True
pidfile = '/var/run/hyperbola-production/gunicorn.pid'
accesslog = '-'
errorlog = '-'
