# Django settings for hyperbola

import os
import warnings

from django.core.exceptions import ImproperlyConfigured


DEBUG = TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['hyperbo.la']

USE_X_FORWARDED_HOST = True

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
BASE_PATH = os.path.dirname(PROJECT_PATH)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(PROJECT_PATH, 'db.cnf'),
        },
    }
}

# Internationalization
# # https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = False

USE_L10N = False

USE_TZ = False

MEDIA_ROOT = '/hyperbola/media/'

MEDIA_URL = '//media.hyperbo.la/'

STATIC_URL = '//assets.hyperbo.la/'

STATIC_ROOT = os.path.join(BASE_PATH, 'assets')

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

FILE_UPLOAD_PERMISSIONS = 0o644

# load SECRET_KEY from local_settings.py

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'email_obfuscator',
    'localflavor',
    'markdown_deux',
    'pipeline',
    'sorl.thumbnail',
    'hyperbola.contact',
    'hyperbola.frontpage',
    'hyperbola.helpers',
    'hyperbola.lifestream',
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

WSGI_APPLICATION = 'hyperbola.wsgi.application'


# Thumbnailing
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.pil_engine.Engine'
THUMBNAIL_FORMAT = 'PNG'
THUMBNAIL_UPSCALE = False


# Asset caching
PIPELINE_ENABLED = True
PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
            'vendor/bootstrap/bootstrap-3.1.1-dist/css/bootstrap.css',
        ),
        'output_filename': 'css/bootstrap.min.css',
    },
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
    'bootstrap': {
        'source_filenames': (
            'vendor/bootstrap/bootstrap-3.1.1-dist/js/bootstrap.js',
        ),
        'output_filename': 'js/bootstrap.min.js',
    },
    'lightbox': {
        'source_filenames': (
            'vendor/bootstrap-lightbox/0.6.2/bootstrap-lightbox.min.js',
        ),
        'output_filename': 'js/bootstrap-lightbox.min.js',
    },
    'retinajs': {
        'source_filenames': (
            'vendor/retinajs/v1.1.0/retina.js',
        ),
        'output_filename': 'js/retina.min.js',
    },
}

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

PIPELINE_YUI_BINARY = '/usr/bin/env yui-compressor'


# determine if we are in the staging environment
try:
    # The presence of this module indicates the staging environment
    from hyperbola.is_staging import *  # NOQA
    ALLOWED_HOSTS = ['staging.hyperbo.la']
    STATIC_URL = ASSETS_URL = '//staging-assets.hyperbo.la/'
    warnings.simplefilter('error', DeprecationWarning)
except ImportError:
    pass

# try to import local settings
# must set SECRET_KEY
try:
    from hyperbola.local_settings import *  # NOQA
except ImportError:
    pass

try:
    SECRET_KEY
except NameError:
    raise ImproperlyConfigured("Must set SECRET_KEY in local_settings.py")
