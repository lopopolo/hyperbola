# Django settings for hyperbola

from enum import Enum, auto
from os import environ
from pathlib import Path


class ConfigLoader:
    def source(self, env, default=None):
        pass

    @property
    def environment(self):
        return Env[self.source('ENVIRONMENT')]


class DotenvLoader(ConfigLoader):
    def __init__(self):
        from dotenv import find_dotenv, load_dotenv
        load_dotenv(find_dotenv())

    def source(self, env, default=None):
        from django.core.exceptions import ImproperlyConfigured
        prop = environ.get(env, default)
        if prop is None:
            raise ImproperlyConfigured('Environment variable {} not set'.format(env))
        if prop == "" and default is not None:
            return default

        return prop


class Env(Enum):
    production = auto()
    stage = auto()
    local = auto()


class EnvironmentConfig(object):
    """Compute environment-specific settings."""

    def __init__(self, loader):
        self.environment = loader.environment
        self.path = self.PathsConfig(self.environment)
        self.secret_key = loader.source('SECRET_KEY')
        self.db = self.DBConfig(loader)
        self.content = self.ContentConfig(self.environment, self.path.root)

    def __str__(self):
        return self.environment.name

    @property
    def allowed_hosts(self):
        if self.environment is Env.production:
            return ['hyperbo.la']
        elif self.environment is Env.stage:
            return ['stage.hyperboladc.net']
        elif self.environment is Env.local:
            return ['local.hyperboladc.net']
        return []

    @property
    def is_admin(self):
        return True

    @property
    def is_secure(self):
        return True

    @property
    def enable_perf_optimizations(self):
        return True

    @property
    def additional_installed_apps(self):
        apps = []
        if self.is_admin:
            apps.append('django.contrib.admin')
        return apps

    @property
    def additional_urls(self):
        from django.urls import path
        urls = []
        if self.is_admin:
            from django.contrib import admin
            urls.append(path('ssb/', admin.site.urls))
        return urls

    @property
    def debug(self):
        return False

    class PathsConfig(object):
        def __init__(self, environment):
            self.package = Path(__file__).resolve().parent
            self.root = Path('/hyperbola/sdist')

    class DBConfig(object):
        def __init__(self, loader):
            self.host = 'mysql.app.hyperboladc.net'
            self.port = '3306'
            self.user = 'app'
            self.password = loader.source('DB_PASSWORD')
            self.name = 'hyperbola'

    class ContentConfig(object):
        def __init__(self, environment, root_path):
            self.static_root = root_path.joinpath('document-root', 'static')
            self.static_dirs = [root_path.joinpath('dist')]
            self.static_url = '/static/'
            if environment is Env.production:
                self.media_bucket_name = 'www.hyperbolausercontent.net'
                self.aws_region = 'us-west-2'
            elif environment in [Env.stage, Env.local]:
                self.media_bucket_name = 'local.hyperbolausercontent.net'
                self.aws_region = 'us-east-1'
            self.media_url = 'https://{}/'.format(self.media_bucket_name)


ENVIRONMENT = EnvironmentConfig(loader=DotenvLoader())

DEBUG = ENVIRONMENT.debug

ALLOWED_HOSTS = ENVIRONMENT.allowed_hosts

USE_X_FORWARDED_HOST = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': ENVIRONMENT.db.name,
        'USER': ENVIRONMENT.db.user,
        'PASSWORD': ENVIRONMENT.db.password,
        'HOST': ENVIRONMENT.db.host,
        'PORT': ENVIRONMENT.db.port,
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

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'hyperbola_app_cache',
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

if ENVIRONMENT.enable_perf_optimizations:
    CONN_MAX_AGE = 5 * 60

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Etc/UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

# Media and Static Files

DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'

AWS_S3_BUCKET_NAME = ENVIRONMENT.content.media_bucket_name
AWS_S3_BUCKET_AUTH = False
AWS_S3_PUBLIC_URL = ENVIRONMENT.content.media_url
AWS_REGION = ENVIRONMENT.content.aws_region

MEDIA_URL = ENVIRONMENT.content.media_url

STATIC_ROOT = str(ENVIRONMENT.content.static_root)

STATIC_URL = ENVIRONMENT.content.static_url

STATICFILES_DIRS = list(map(str, ENVIRONMENT.content.static_dirs))

STATICFILES_STORAGE = 'hyperbola.core.static.HyperbolaManifestStorage'

FILE_UPLOAD_PERMISSIONS = 0o644

SECRET_KEY = ENVIRONMENT.secret_key

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mysql',
    'django_s3_storage',
    'stdimage',
    'hyperbola.contact',
    'hyperbola.core',
    'hyperbola.frontpage',
    'hyperbola.lifestream',
    'hyperbola.shortlinks',
] + ENVIRONMENT.additional_installed_apps

MIDDLEWARE = [
    'hyperbola.core.middleware.HealthCheckMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'hyperbola.core.middleware.FQDNMiddleware',
]

_template_loader = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]
if ENVIRONMENT.enable_perf_optimizations:
    _template_loader = [(
        'django.template.loaders.cached.Loader',
        _template_loader
    )]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(ENVIRONMENT.path.package.joinpath('templates')),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': _template_loader,
        },
    },
]

ROOT_URLCONF = 'hyperbola.urls'

WSGI_APPLICATION = 'hyperbola.wsgi.application'

# Security
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = ENVIRONMENT.is_secure
SECURE_REDIRECT_EXEMPT = ['healthz']
SESSION_COOKIE_SECURE = ENVIRONMENT.is_secure
CSRF_COOKIE_SECURE = ENVIRONMENT.is_secure
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 20,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[contactor] %(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        # Send all messages to console
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # This is the "catch all" logger
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
