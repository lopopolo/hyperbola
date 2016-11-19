import multiprocessing

bind = 'unix:/var/run/hyperbola-production/hyperbola-production.sock'
workers = multiprocessing.cpu_count() + 1
pidfile = '/var/run/hyperbola-production/gunicorn.pid'
accesslog = '-'
errorlog = '-'
capture_output = True
