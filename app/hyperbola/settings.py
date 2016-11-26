# Django settings for hyperbola

import os
from enum import Enum, unique


@unique
class Env(Enum):
    production = 'production'
    staging = 'staging'
    dev = 'dev'

    @classmethod
    def source(cls, env, default=None):
        from django.core.exceptions import ImproperlyConfigured
        prop = os.environ.get(env, default)
        if prop is None:
            raise ImproperlyConfigured('Environment variable {0} not set'.format(env))

        if isinstance(prop, str) and prop.strip().lower() in ['1', 'true', 'yes', 'on']:
            return True
        elif isinstance(prop, str) and prop.strip().lower() in ['0', 'false', 'no', 'off']:
            return False
        else:
            return prop

    @classmethod
    def make(cls, env):
        """
        Construct an Env by loading the environment constant from an env variable.

        :rtype: Env
        """
        environment = cls.source(env)
        return cls(environment)


class EnvironmentConfig(object):
    """Compute environment-specific settings."""

    def __init__(self, root_path):
        self.environment = Env.make('ENVIRONMENT')
        self.secret_key = Env.source('SECRET_KEY')
        self.db = self.DBConfig()
        self.content = self.ContentConfig(self.environment, root_path)
        self.email_backup = self.EmailBackupConfig()

    @property
    def redis_enabled(self):
        return self.environment in [Env.production, Env.staging]

    @property
    def allowed_hosts(self):
        if self.environment is Env.production:
            return ['hyperbo.la']
        elif self.environment is Env.staging:
            return ['staging.hyperbo.la']
        return ['localhost', '127.0.0.1', '[::1]']

    @property
    def is_secure(self):
        return self.environment in [Env.production, Env.staging]

    @property
    def additional_installed_apps(self):
        apps = []
        if self.environment in [Env.production, Env.dev]:
            apps.extend(['django.contrib.admin'])
        if self.environment is Env.dev:
            apps.extend(['debug_toolbar', 'template_timings_panel'])
        return apps

    @property
    def additional_urls(self):
        from django.conf.urls import include, url
        urls = []
        if self.environment in [Env.production, Env.dev]:
            from django.contrib import admin
            # only enable admin urls in production and dev
            urls.extend([url(r'^ssb/', admin.site.urls)])
        if self.environment is Env.dev:
            import debug_toolbar
            from django.conf.urls.static import static
            urls.extend(static(MEDIA_URL, document_root=MEDIA_ROOT))
            urls.extend([url(r'^__debug__/', include(debug_toolbar.urls))])
        return urls

    @property
    def debug(self):
        if self.environment is Env.dev:
            return True
        if self.environment is Env.staging:
            return Env.source('DEBUG', False)
        return False

    class DBConfig(object):
        def __init__(self):
            self.name = Env.source('DB_NAME')
            self.user = Env.source('DB_USER')
            self.password = Env.source('DB_PASSWORD')
            self.host = Env.source('DB_HOST')
            self.port = Env.source('DB_PORT')

    class ContentConfig(object):
        def __init__(self, environment, root_path):
            self.media_root = os.path.join(root_path, 'media', environment.value)
            self.static_root = os.path.join(root_path, 'assets')
            if environment in [Env.production, Env.staging]:
                self.media_url = 'https://www.hyperbolacdn.com/hyperbolausercontent/'
                self.static_url = 'https://www.hyperbolacdn.com/assets/{}/'.format(environment.value)
            else:
                self.media_url = '/media/'
                self.static_url = '/static/'

    class EmailBackupConfig(object):
        def __init__(self):
            self.username = Env.source('BACKUP_EMAIL_LOGIN_USERNAME')
            self.password = Env.source('BACKUP_EMAIL_LOGIN_PASSWORD')


PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
ROOT_PATH = os.path.dirname(os.path.dirname(PROJECT_PATH))

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

if ENVIRONMENT.redis_enabled:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        },
        'imagekit': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/2',
            'TIMEOUT': None,
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }
    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
    SESSION_CACHE_ALIAS = 'default'
    IMAGEKIT_CACHE_BACKEND = 'imagekit'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Etc/UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

# Media and Static Files

MEDIA_ROOT = ENVIRONMENT.content.media_root

MEDIA_URL = ENVIRONMENT.content.media_url

STATIC_ROOT = ENVIRONMENT.content.static_root

STATIC_URL = ENVIRONMENT.content.static_url

STATICFILES_DIRS = [
    os.path.join(PROJECT_PATH, 'static'),
]

STATICFILES_STORAGE = 'hyperbola.core.static.PipelineManifestStorage'

FILE_UPLOAD_PERMISSIONS = 0o644

SECRET_KEY = ENVIRONMENT.secret_key

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
] + ENVIRONMENT.additional_installed_apps

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
SECURE_SSL_REDIRECT = ENVIRONMENT.is_secure
SECURE_REDIRECT_EXEMPT = ['healthz']
SESSION_COOKIE_SECURE = ENVIRONMENT.is_secure
CSRF_COOKIE_SECURE = ENVIRONMENT.is_secure
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# backups
BACKUP_EMAIL_LOGIN_USERNAME = ENVIRONMENT.email_backup.username
BACKUP_EMAIL_LOGIN_PASSWORD = ENVIRONMENT.email_backup.password

# Environment-specific configuration
if ENVIRONMENT.environment is Env.dev:
    SENDFILE_BACKEND = 'sendfile.backends.development'
    PIPELINE['PIPELINE_ENABLED'] = False
    # debug toolbar
    from debug_toolbar.settings import PANELS_DEFAULTS as _PANEL_DEFAULTS
    DEBUG_TOOLBAR_PANELS = _PANEL_DEFAULTS + ['template_timings_panel.panels.TemplateTimings.TemplateTimings']
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = ['127.0.0.1']
