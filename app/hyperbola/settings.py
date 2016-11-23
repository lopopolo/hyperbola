# Django settings for hyperbola

import os

from django.core.exceptions import ImproperlyConfigured


def source(env, default=None):
    prop = os.environ.get(env, default)
    if prop is None:
        raise ImproperlyConfigured('Environment variable {0} not set'.format(env))

    if prop in ['yes', 'true']:
        return True
    elif prop in ['no', 'false']:
        return False
    else:
        return prop

ENVIRONMENT = source('ENVIRONMENT')

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
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            # Create database with:
            # > create database hyperbola character set UTF8mb4 collate utf8mb4_unicode_ci;
            'charset': 'utf8mb4',
        },
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        }
    }
}

if ENVIRONMENT in ['production', 'staging']:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }
    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
    SESSION_CACHE_ALIAS = 'default'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = False

USE_L10N = False

USE_TZ = False

# Media and Static Files

MEDIA_ROOT = os.path.join(ROOT_PATH, 'media', ENVIRONMENT)

MEDIA_URL = 'https://www.hyperbolacdn.com/hyperbolausercontent/'

STATIC_ROOT = os.path.join(ROOT_PATH, 'assets')

STATIC_URL = 'https://www.hyperbolacdn.com/assets/{}/'.format(ENVIRONMENT)

STATICFILES_DIRS = [
    os.path.join(PROJECT_PATH, 'static'),
]

STATICFILES_STORAGE = 'hyperbola.core.static.PipelineManifestStorage'

FILE_UPLOAD_PERMISSIONS = 0o644

SECRET_KEY = source('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mysql',
    'imagekit',
    'localflavor',
    'markdown_deux',
    'pipeline',
    'hyperbola.contact',
    'hyperbola.core',
    'hyperbola.frontpage',
    'hyperbola.lifestream',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'hyperbola.core.middleware.FQDNMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_PATH, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]

ROOT_URLCONF = 'hyperbola.urls'

WSGI_APPLICATION = 'hyperbola.wsgi.application'

# Thumbnailing

IMAGEKIT_CACHEFILE_DIR = 'cache/g'
IMAGEKIT_CACHEFILE_NAMER = 'hyperbola.core.hash_with_extension'

# Asset caching
PIPELINE = {
    'PIPELINE_ENABLED': True,
    'STYLESHEETS': {
        'sitewide': {
            'source_filenames': (
                'css/bootstrap.purified.css',
                'css/sitewide.css',
            ),
            'output_filename': 'css/sitewide.min.css',
        },
    },
    'CSS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',
}

# Sendfile
# https://github.com/johnsensible/django-sendfile#nginx-backend
SENDFILE_BACKEND = 'sendfile.backends.nginx'
SENDFILE_ROOT = MEDIA_ROOT
SENDFILE_URL = '/media'

# Security
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True if ENVIRONMENT in ['production', 'staging'] else False
SECURE_REDIRECT_EXEMPT = ['/healthz']
SESSION_COOKIE_SECURE = True if ENVIRONMENT in ['production', 'staging'] else False
CSRF_COOKIE_SECURE = True if ENVIRONMENT in ['production', 'staging'] else False
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# backups
BACKUP_EMAIL_LOGIN_USERNAME = source('BACKUP_EMAIL_LOGIN_USERNAME')
BACKUP_EMAIL_LOGIN_PASSWORD = source('BACKUP_EMAIL_LOGIN_PASSWORD')

# Environment-specific configuration
if ENVIRONMENT == 'production':
    DEBUG = False
    ALLOWED_HOSTS = ['hyperbo.la']
    # enable admin interface only on production
    INSTALLED_APPS.append('django.contrib.admin')
elif ENVIRONMENT == 'staging':
    DEBUG = source('DEBUG', False)
    ALLOWED_HOSTS = ['staging.hyperbo.la']
elif ENVIRONMENT == 'dev':
    DEBUG = True
    MEDIA_URL = '/media/'
    SENDFILE_BACKEND = 'sendfile.backends.development'
    PIPELINE['PIPELINE_ENABLED'] = False
    STATIC_URL = '/static/'
    # enable admin interface in dev (sandbox)
    INSTALLED_APPS.append('django.contrib.admin')
    # debug toolbar
    from debug_toolbar.settings import PANELS_DEFAULTS as _PANEL_DEFAULTS
    INSTALLED_APPS.extend(['debug_toolbar', 'template_timings_panel'])
    DEBUG_TOOLBAR_PANELS = _PANEL_DEFAULTS + ['template_timings_panel.panels.TemplateTimings.TemplateTimings']
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = ['127.0.0.1']
else:
    raise ImproperlyConfigured('Invalid ENVIRONMENT: {0}'.format(ENVIRONMENT))
