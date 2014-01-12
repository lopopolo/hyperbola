# Django settings for hyperbola

import os

# these may be overridden by is_staging or local_settings
DEBUG = TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['hyperbo.la']

USE_X_FORWARDED_HOST = True

# This dynamically discovers the path to the project
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
BASE_PATH = REPO_PATH = os.path.dirname(PROJECT_PATH)

ADMINS = (
    ('Ryan Lopopolo', 'rjl@hyperbo.la'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
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

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/hyperbola/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '//media.hyperbo.la/'

STATIC_URL = ASSETS_URL = '//assets.hyperbo.la/'

STATIC_ROOT = os.path.join(REPO_PATH, 'assets')

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

FILE_UPLOAD_PERMISSIONS = 0644

# Make this unique, and don't share it with anybody.
# SECRET_KEY = SOME_VALUE
# load this from local_settings.py

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'localflavor',
    'pipeline',
    'sorl.thumbnail',
    'hyperbola.contact',
    'hyperbola.frontpage',
    'hyperbola.lifestream',
    'hyperbola.helpers',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_LOADERS = (
    (
        'django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ),
    ),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

ROOT_URLCONF = 'hyperbola.urls'


# Thumbnailing
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.pil_engine.Engine'
THUMBNAIL_FORMAT = 'PNG'
THUMBNAIL_UPSCALE = False


PIPELINE_ENABLED = True
PIPELINE_CSS = {
    'lightbox': {
        'source_filenames': (
            'vendor/bootstrap-lightbox/0.6.2/bootstrap-lightbox.min.css',
        ),
        'output_filename': 'css/bootstrap-lightbox.min.css',
    },
    'sitewide': {
        'source_filenames': (
            'css/sitewide.css',
        ),
        'output_filename': 'css/sitewide.min.css',
    },
}

PIPELINE_JS = {
    'lightbox': {
        'source_filenames': (
            'vendor/bootstrap-lightbox/0.6.2/bootstrap-lightbox.min.js',
        ),
        'output_filename': 'js/bootstrap-lightbox.min.js',
    },
}

# When PIPELINE is True, CSS and JavaScripts will be concatenated and filtered.
# When False, the source-files will be used instead.
# Default: PIPELINE = not DEBUG

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

PIPELINE_YUI_BINARY = '/usr/bin/env yui-compressor'


# determine if we are in the staging environment
try:
    from is_staging import *  # NOQA
    ALLOWED_HOSTS = ['staging.hyperbo.la']
    STATIC_URL = ASSETS_URL = '//staging-assets.hyperbo.la/'
    import warnings
    warnings.simplefilter('error', DeprecationWarning)
except ImportError:
    pass

# try to import local settings
# must set SECRET_KEY
from local_settings import *  # NOQA

try:
    SECRET_KEY
except NameError:
    raise "Must set SECRET_KEY in local_settings.py"
