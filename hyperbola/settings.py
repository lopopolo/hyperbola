# Django settings for hyperbola

from datetime import timedelta
from enum import Enum, auto
from os import environ
from pathlib import Path


class ConfigLoader:
    def source(self, env, default=None):
        pass

    @property
    def environment(self):
        return Env[environ.get("ENVIRONMENT")]


class ParameterStoreLoader(ConfigLoader):
    def __init__(self):
        from ssm_parameter_store import EC2ParameterStore

        store = EC2ParameterStore(region_name=self._region)
        self.parameters = store.get_parameters_by_path(
            f"/app/{self.environment.name}/", recursive=True, decrypt=True
        )

    def source(self, config, default=None):
        from django.core.exceptions import ImproperlyConfigured

        prop = self.parameters.get(config, default)
        if prop is None:
            raise ImproperlyConfigured(f"{config} not found in parameter store")

        return prop

    @property
    def _region(self):
        if self.environment in [Env.stage, Env.local]:
            return "us-east-1"
        return "us-west-2"


class Env(Enum):
    production = auto()
    stage = auto()
    local = auto()


class EnvironmentConfig:
    """Compute environment-specific settings."""

    def __init__(self, *, loader):
        self.environment = loader.environment
        self.aws = self.AWSConfig(self.environment)
        self.path = self.PathsConfig(self.environment)
        self.secret_key = loader.source("SECRET_KEY")
        self.db = self.DBConfig(loader)
        self.content = self.ContentConfig(self.environment, self.path)

    def __str__(self):
        return self.environment.name

    @property
    def allowed_hosts(self):
        if self.environment is Env.production:
            return ["hyperbo.la"]
        elif self.environment is Env.stage:
            return ["stage.hyperboladc.net"]
        elif self.environment is Env.local:
            return ["local.hyperboladc.net"]
        return []

    @property
    def is_admin(self):
        return True

    @property
    def is_secure(self):
        return True

    @property
    def enable_optimizations(self):
        return True

    @property
    def additional_installed_apps(self):
        apps = []
        if self.is_admin:
            apps.append("django.contrib.admin")
        return apps

    @property
    def additional_urls(self):
        from django.urls import path

        urls = []
        if self.is_admin:
            from django.contrib import admin

            urls.append(path("ssb/", admin.site.urls))
        return urls

    @property
    def debug(self):
        return False

    class AWSConfig:
        def __init__(self, environment):
            if environment is Env.production:
                self.region = "us-west-2"
            elif environment in [Env.stage, Env.local]:
                self.region = "us-east-1"

    class PathsConfig:
        def __init__(self, environment):
            self.package = Path(__file__).resolve().parent
            self.root = self.package.parent
            self.sdist = Path("/hyperbola/sdist")

    class DBConfig:
        def __init__(self, loader):
            self.host = "mysql.app.hyperboladc.net"
            self.port = "3306"
            self.user = "app"
            self.password = loader.source("DB_PASSWORD")
            self.name = "hyperbola"

    class ContentConfig:
        def __init__(self, environment, paths):
            self.static_root = paths.root.joinpath("assets")
            self.static_dirs = [paths.sdist.joinpath("dist")]
            self.static_url = "/"
            if environment is Env.production:
                self.media_bucket_name = "www.hyperbolausercontent.net"
            elif environment in [Env.stage, Env.local]:
                self.media_bucket_name = "local.hyperbolausercontent.net"
            self.media_url = f"https://{self.media_bucket_name}/"


# Deployment
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

ENVIRONMENT = EnvironmentConfig(loader=ParameterStoreLoader())

SECRET_KEY = ENVIRONMENT.secret_key

DEBUG = ENVIRONMENT.debug

ALLOWED_HOSTS = ENVIRONMENT.allowed_hosts

# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_mysql",
    "django_s3_storage",
    "stdimage",
    "hyperbola.blog",
    "hyperbola.contact",
    "hyperbola.core",
    "hyperbola.frontpage",
    "hyperbola.lifestream",
    "hyperbola.shortlinks",
] + ENVIRONMENT.additional_installed_apps

MIDDLEWARE = [
    "hyperbola.core.middleware.HealthCheckMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "hyperbola.core.middleware.FQDNMiddleware",
]

ROOT_URLCONF = "hyperbola.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(ENVIRONMENT.path.package.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "hyperbola.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": ENVIRONMENT.db.name,
        "USER": ENVIRONMENT.db.user,
        "PASSWORD": ENVIRONMENT.db.password,
        "HOST": ENVIRONMENT.db.host,
        "PORT": ENVIRONMENT.db.port,
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": timedelta(minutes=5).seconds if ENVIRONMENT.enable_optimizations else 0,
        "OPTIONS": {
            # Create database with:
            # > create database hyperbola character set UTF8mb4 collate utf8mb4_unicode_ci;
            "charset": "utf8mb4",
            "connect_timeout": timedelta(seconds=5).seconds,
        },
        "TEST": {"CHARSET": "utf8mb4", "COLLATION": "utf8mb4_unicode_ci"},
    }
}


# Cache
# https://docs.djangoproject.com/en/2.1/topics/cache/

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "hyperbola_app_cache",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

SESSION_CACHE_ALIAS = "default"


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 20},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = str(ENVIRONMENT.content.static_root)

STATIC_URL = ENVIRONMENT.content.static_url

STATICFILES_DIRS = list(map(str, ENVIRONMENT.content.static_dirs))

STATICFILES_STORAGE = "hyperbola.core.static.HyperbolaManifestStorage"


# Media
# https://docs.djangoproject.com/en/2.1/topics/files/

AWS_S3_BUCKET_NAME = ENVIRONMENT.content.media_bucket_name

AWS_S3_BUCKET_AUTH = False

AWS_S3_PUBLIC_URL = ENVIRONMENT.content.media_url

AWS_REGION = ENVIRONMENT.aws.region

DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"

MEDIA_URL = ENVIRONMENT.content.media_url

FILE_UPLOAD_PERMISSIONS = 0o644


# Security
# https://docs.djangoproject.com/en/2.1/topics/security/

USE_X_FORWARDED_HOST = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = ENVIRONMENT.is_secure

SECURE_REDIRECT_EXEMPT = ["healthz"]

SESSION_COOKIE_SECURE = ENVIRONMENT.is_secure

CSRF_COOKIE_SECURE = ENVIRONMENT.is_secure

CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = "DENY"


# Logging
# https://docs.djangoproject.com/en/2.1/topics/logging/
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {"verbose": {"format": "[contactor] %(levelname)s %(asctime)s %(message)s"}},
    "handlers": {
        # Send all messages to console
        "console": {"level": "WARNING", "class": "logging.StreamHandler"}
    },
    "loggers": {
        # This is the "catch all" logger
        "": {"handlers": ["console"], "level": "INFO", "propagate": False}
    },
}
