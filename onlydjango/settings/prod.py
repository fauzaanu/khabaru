import os

from .base import *
from huey import RedisHuey

DEBUG = False
ALLOWED_HOSTS = [
    os.getenv("ALLOWED_HOST", "khabaru.onlydjango"),
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = [
    'https://storage.khabaru.onlydjango',
]
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "default_secret_key")

CSRF_TRUSTED_ORIGINS = [
    os.getenv("CSRF_TRUSTED_ORIGIN", "https://khabaru.onlydjango"),
]
CSRF_COOKIE_DOMAIN = os.getenv("CSRF_COOKIE_DOMAIN", ".khabaru.onlydjango")
SESSION_COOKIE_DOMAIN = os.getenv("SESSION_COOKIE_DOMAIN", ".khabaru.onlydjango")
CSRF_COOKIE_SECURE = bool(os.getenv("CSRF_COOKIE_SECURE", True))

# Use any S3 Compatible storage backend for static and media files
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME", "default_bucket_name")
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL", "https://default.endpoint.url")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "default_access_key_id")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "default_secret_access_key")
AWS_S3_SIGNATURE_VERSION = os.getenv("AWS_S3_SIGNATURE_VERSION", "s3v4")
AWS_S3_CUSTOM_DOMAIN = os.getenv("AWS_S3_CUSTOM_DOMAIN", "https://default.custom.domain")

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {},
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {},
    },
    "media": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {},
    },
}

STATIC_URL = os.getenv("STATIC_URL", "static/")
STATIC_ROOT = os.path.join(BASE_DIR, os.getenv("STATIC_ROOT", "staticfiles"))
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, os.getenv("STATICFILES_DIR", "static")),
]

# For Django all auth
ACCOUNT_DEFAULT_HTTP_PROTOCOL = os.getenv("ACCOUNT_DEFAULT_HTTP_PROTOCOL", "https")

# Database
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.getenv("PGDATABASE", "default_db_name"),
        "USER": os.getenv("PGUSER", "default_user"),
        "PASSWORD": os.getenv("PGPASSWORD", "default_password"),
        "HOST": os.getenv("PGHOST", "localhost"),
        "PORT": os.getenv("PGPORT", "5432"),
        "OPTIONS": {
            "pool": {
                "min_size": int(os.getenv("DB_POOL_MIN_SIZE", 2)),
                "max_size": int(os.getenv("DB_POOL_MAX_SIZE", 4)),
                "timeout": int(os.getenv("DB_POOL_TIMEOUT", 10)),
            }
        },
    }
}

# Cache settings
REDIS_URL = os.getenv("REDIS_PRIVATE_URL", "redis://localhost:6379/0")
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": [
            REDIS_URL,
        ],
        "KEY_PREFIX": os.getenv("CACHE_KEY_PREFIX", "default_site_name"),
    }
}

HUEY = RedisHuey("huey", url=REDIS_URL)

# Email to receive error logs
ADMINS = [("Admin", os.getenv("ADMIN_EMAIL", "admin@example.com"))]

# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = bool(os.getenv("EMAIL_USE_TLS", True))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "default_email_user")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "default_email_password")

# Setup logging - log to file and email
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "telegram": {
            "level": "INFO",
            "class": "onlydjango.telegram_logging.TelegramBotHandler",
            "telegram_bot_token": os.getenv("TELEGRAM_BOT_TOKEN", "default_telegram_token"),
            "telegram_chat_id": os.getenv("TELEGRAM_CHAT_ID", "default_telegram_chat_id"),
            "formatter": "telegram",
            "filters": ["exclude_disallowed_host"],
        },
        "error_handler": {
            "level": "ERROR",
            "class": "onlydjango.telegram_logging.TelegramBotHandler",
            "telegram_bot_token": os.getenv("TELEGRAM_BOT_TOKEN", "default_telegram_token"),
            "telegram_chat_id": os.getenv("TELEGRAM_CHAT_ID", "default_telegram_chat_id"),
            "formatter": "telegram",
            "filters": ["exclude_disallowed_host"],
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "formatters": {
        "telegram": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "root": {
        "handlers": ["error_handler", "console"],
        "level": "INFO",
        "propagate": True,
    },
    "loggers": {
        "django.security.DisallowedHost": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
    "filters": {
        "exclude_disallowed_host": {
            "()": "django.utils.log.CallbackFilter",
            "callback": lambda record: not record.name.startswith("django.security.DisallowedHost"),
        },
    },
}
