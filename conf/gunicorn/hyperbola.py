import multiprocessing

bind = 'unix:/hyperbola/var/sock/hyperbola-live.sock'
workers = multiprocessing.cpu_count() + 1

accesslog = '/hyperbola/var/log/gunicorn/live.access'
errorlog = '/hyperbola/var/log/gunicorn/live.error'
