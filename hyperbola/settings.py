# Django settings for hyperbola

from enum import Enum, unique
from os import environ
from pathlib import Path


@unique
class Env(Enum):
    production = 'production'
    local = 'local'
    dev = 'dev'

    @classmethod
    def source(cls, env, default=None):
        from django.core.exceptions import ImproperlyConfigured
        prop = environ.get(env, default)
        if prop is None:
            raise ImproperlyConfigured('Environment variable {} not set'.format(env))
        if prop == "" and default is not None:
            return default

        if isinstance(prop, str) and prop.strip().lower() in ['1', 'true', 'yes', 'on']:
            return True
        if isinstance(prop, str) and prop.strip().lower() in ['0', 'false', 'no', 'off']:
            return False
        return prop

    @classmethod
    def make(cls, env, root_path):
        """
        Construct an Env by loading the environment constant from an env variable.

        :rtype: Env
        """
        from dotenv import load_dotenv
        load_dotenv(str(root_path.joinpath('.env')))
        environment = cls.source(env)
        return cls(environment)


class EnvironmentConfig(object):
    """Compute environment-specific settings."""

    def __init__(self, root_path):
        self.environment = Env.make('HYPERBOLA_ENVIRONMENT', root_path)
        self.secret_key = Env.source('SECRET_KEY')
        self.db = self.DBConfig()
        self.content = self.ContentConfig(self.environment, root_path)

    def __str__(self):
        return self.environment.value

    @property
    def allowed_hosts(self):
        if self.environment is Env.production:
            return ['hyperbo.la']
        elif self.environment is Env.local:
            return ['app-local.hyperboladc.net']
        return ['localhost', '127.0.0.1', '[::1]']

    @property
    def is_secure(self):
        return self.environment in [Env.production]

    @property
    def additional_installed_apps(self):
        apps = []
        if self.environment in [Env.production, Env.local, Env.dev]:
            apps.extend(['django.contrib.admin'])
        if self.environment is Env.dev:
            apps.extend(['debug_toolbar', 'template_timings_panel'])
        return apps

    @property
    def additional_urls(self):
        from django.conf.urls import include, url
        urls = []
        if self.environment in [Env.production, Env.local, Env.dev]:
            from django.contrib import admin
            # only enable admin urls in production and dev
            urls.extend([url(r'^ssb/', admin.site.urls)])
        if self.environment is Env.dev:
            import debug_toolbar
            urls.extend([url(r'^__debug__/', include(debug_toolbar.urls))])
        if self.environment in [Env.local, Env.dev]:
            from django.conf.urls.static import static
            urls.extend(static(MEDIA_URL, document_root=MEDIA_ROOT))
        return urls

    @property
    def debug(self):
        if self.environment in [Env.local, Env.dev]:
            return True
        return False

    class DBConfig(object):
        def __init__(self):
            self.host = Env.source('DB_HOST')
            self.port = Env.source('DB_PORT')
            self.user = Env.source('DB_USER')
            self.password = Env.source('DB_PASSWORD')
            self.name = Env.source('DB_NAME')

    class ContentConfig(object):
        def __init__(self, environment, root_path):
            self.media_root = root_path.joinpath('media', environment.value)
            self.static_root = root_path.joinpath('document-root', 'static')
            self.static_dirs = [root_path.joinpath('dist')]
            self.static_url = '/static/'
            if environment in [Env.production]:
                self.media_bucket_name = 'www.hyperbolausercontent.net'
                self.aws_region = 'us-west-2'
            elif environment in [Env.local, Env.dev]:
                self.media_bucket_name = 'local.hyperbolausercontent.net'
                self.aws_region = 'us-east-1'
            self.media_url = 'https://{}/'.format(self.media_bucket_name)


PACKAGE_PATH = Path(__file__).resolve().parent
ROOT_PATH = Path(Env.source('HYPERBOLA_ROOT_PATH', '/hyperbola/app/current')).resolve()

ENVIRONMENT = EnvironmentConfig(ROOT_PATH)

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

MEDIA_ROOT = str(ENVIRONMENT.content.media_root)

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
    'localflavor',
    'stdimage',
    'hyperbola.contact',
    'hyperbola.core',
    'hyperbola.frontpage',
    'hyperbola.lifestream',
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(PACKAGE_PATH.joinpath('templates')),
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

# Security
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
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

# Environment-specific configuration
if ENVIRONMENT.environment is Env.dev:
    # debug toolbar
    from debug_toolbar.settings import PANELS_DEFAULTS as _PANEL_DEFAULTS
    DEBUG_TOOLBAR_PANELS = _PANEL_DEFAULTS + \
        ['template_timings_panel.panels.TemplateTimings.TemplateTimings']
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = ['127.0.0.1']
    HYPERBOLA_S3_BACKUP_BUCKET = 'hyperbola-app-backup-local'
    if False:  # pylint: disable=using-constant-test
        # workaround for intellij dying on dynamically-created INSTALLED_APPS
        # https://stackoverflow.com/a/42672633
        INSTALLED_APPS = [
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django_mysql',
            'django_s3_storage',
            'localflavor',
            'missing',
            'stdimage',
            'hyperbola.contact',
            'hyperbola.core',
            'hyperbola.frontpage',
            'hyperbola.lifestream',
        ]
        # workaround for intellij dying on dynamically-created STATIC_ROOT
        STATIC_ROOT = 'dist'
