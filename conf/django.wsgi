import os
import sys

# setup PYTHONPATH and env vars for apache
sys.path.append('/var/www/hyperbola/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'hyperbola.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

