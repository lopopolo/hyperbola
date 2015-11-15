# Django settings for hyperbola

import os
import warnings

from django.core.exceptions import ImproperlyConfigured


def source(env):
    prop = os.environ.get(env)
    if prop is None:
        raise ImproperlyConfigured(
            'Environment variable {0} not set'.format(env))

    if prop in ['yes', 'true']:
        return True
    elif prop in ['no', 'false']:
        return False
    else:
        return prop

USE_X_FORWARDED_HOST = True

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
ROOT_PATH = os.path.dirname(os.path.dirname(PROJECT_PATH))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': source('DB_NAME'),
        'USER': source('DB_USER'),
        'PASSWORD': source('DB_PASSWORD'),
        'HOST': source('DB_HOST'),
        'PORT': source('DB_PORT'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = False

USE_L10N = False

USE_TZ = False

# Media and Static Files

MEDIA_ROOT = '/hyperbola/media/'

MEDIA_URL = '//media.hyperbo.la/'

STATIC_URL = '//assets.hyperbo.la/'

STATIC_ROOT = os.path.join(ROOT_PATH, 'assets')

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

FILE_UPLOAD_PERMISSIONS = 0o644


SECRET_KEY = source('SECRET_KEY')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_PATH, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

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
    'lightbox': {
        'source_filenames': (
            'vendor/bootstrap-lightbox/0.6.2/bootstrap-lightbox.min.css',
        ),
        'output_filename': 'css/bootstrap-lightbox.min.css',
    },
    'sitewide': {
        'source_filenames': (
            'vendor/bootstrap/bootstrap-3.3.5-dist/css/bootstrap.css',
            'css/sitewide.css',
        ),
        'output_filename': 'css/sitewide.min.css',
    },
}

PIPELINE_JS = {
    'bootstrap': {
        'source_filenames': (
            'vendor/bootstrap/bootstrap-3.3.5-dist/js/bootstrap.js',
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
            'vendor/retinajs/v1.3.0/retina.js',
        ),
        'output_filename': 'js/retina.min.js',
    },
}

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

PIPELINE_YUI_BINARY = '/usr/bin/env yui-compressor'


# Environment-specific configuration

ENVIRONMENT = source('ENVIRONMENT')

if ENVIRONMENT == 'production':
    DEBUG = False
    ALLOWED_HOSTS = ['hyperbo.la']
    # enable admin interface only on production
    INSTALLED_APPS += (
        'django.contrib.admin',
        'django.contrib.admindocs',
    )
elif ENVIRONMENT == 'staging':
    try:
        DEBUG = source('DEBUG')
    except ImproperlyConfigured:
        DEBUG = False

    ALLOWED_HOSTS = ['staging.hyperbo.la']
    STATIC_URL = '//staging-assets.hyperbo.la/'

    warnings.simplefilter('error', DeprecationWarning)
elif ENVIRONMENT == 'dev':
    DEBUG = True
    PIPELINE_ENABLED = False
    STATIC_URL = '/static/'
    INSTALLED_APPS += (
        'django.contrib.admin',
        'django.contrib.admindocs',
    )

    warnings.simplefilter('error', DeprecationWarning)
else:
    raise ImproperlyConfigured('Invalid ENVIRONMENT: {0}'.format(ENVIRONMENT))
