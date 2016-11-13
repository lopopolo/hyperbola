bind = 'unix:/var/run/hyperbola-staging/hyperbola-staging.sock'
workers = 1
daemon = True
pidfile = '/var/run/hyperbola-staging/gunicorn.pid'
accesslog = '-'
errorlog = '-'
capture_output = True
