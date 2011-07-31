# Django settings for hyperbola

import os
import socket

# Set DEBUG = True if on the production server
if socket.gethostname() == 'hyperbox':
  DEBUG = False
else:
  DEBUG = True

# This dynamically discovers the path to the project
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
REPO_PATH = os.path.join(PROJECT_PATH, '..')

ADMINS = (
  ('Ryan Lopopolo', 'rjl@hyperbo.la'),
)

MANAGERS = ADMINS

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'OPTIONS' : {
      'read_default_file': os.path.join(PROJECT_PATH, 'db.cnf'),
    },
  }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(REPO_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://linode-media.hyperbo.la/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://linode-assets.hyperbo.la/django-media/'

ASSETS_URL = 'http://linode-assets.hyperbo.la'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y$6axl8$tcm)&h!s2i0y3dvy8fdyz(mty&_!w3pr@5)if-rj@2'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
  # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.core.context_processors.debug',
  'django.contrib.auth.context_processors.auth',
)

MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'hyperbola.urls'

TEMPLATE_DIRS = (
  # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
  # Always use forward slashes, even on Windows.
  # Don't forget to use absolute paths, not relative paths.
  os.path.join(PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.admin',
  # 'django.contrib.admindocs',
  'hyperbola.contact',
  'hyperbola.frontpage',
  'hyperbola.lifestream',
  'hyperbola.helpers',
)
