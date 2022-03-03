"""
Django settings for {{cookiecutter.project_slug}} project.
"""

import os
import environ
from datetime import timedelta

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = environ.Path(__file__) - 3
APPS_DIR = BASE_DIR.path('{{cookiecutter.project_slug}}')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='!!!SET DJANGO_SECRET_KEY!!!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1', '*']

CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    '{{cookiecutter.project_slug}}.user.apps.UserConfig',
    '{{cookiecutter.project_slug}}.product.apps.ProductConfig',
    # APPEND_NEW_APP #
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    {%- if cookiecutter.use_whitenoise == 'y' %}
    'whitenoise.middleware.WhiteNoiseMiddleware',
    {%- endif %}
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR.path('templates')), ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# ------------------------------------------------------------------------------

{%- if cookiecutter.use_postgres == "y" %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME', default='{{cookiecutter.project_slug}}'),
        'USER': env('DB_USER', default='dev'),
        'PASSWORD': env('DB_PASS', default='dev'),
        'HOST': env('DB_HOST', default='127.0.0.1'),
        'PORT': env('DB_PORT', default=5432),
    },
}
{%- else %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(str(BASE_DIR), 'dbs/db.sqlite3'),
    }
}
{%- endif %}

# DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://:dev@127.0.0.1:6379/0',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

AUTH_USER_MODEL = 'user.User'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR('staticfiles'))
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Media
# ------------------------------------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR('media')

{% if cookiecutter.use_celery == 'y' -%}
# Celery
# ------------------------------------------------------------------------------
if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE

CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='redis://:dev@127.0.0.1:6379/1')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_IGNORE_RESULT = True

# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 30 * 60 # (seconds)
CELERY_TASK_TIME_LIMIT = CELERY_TASK_SOFT_TIME_LIMIT + 5 * 60
CELERY_RESULT_EXPIRES = 24 * 60 * 60  # 1 day

CELERY_WORKER_PREFETCH_MULTIPLIER = 4

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

{%- endif %}
# Config Logging
# ------------------------------------------------------------------------------


LOG_DIR = env('LOG_DIR', default=str(BASE_DIR.path('logs')))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s.%(funcName)s:%(lineno)d] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(message)s'
        },
        'simple-time': {
            'format': '%(levelname)s [%(asctime)s+0000] %(module)s %(message)s'
        }
    },
    'handlers': {
        'apps-file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + '/apps.log',
            'formatter': 'verbose',
            'maxBytes': 10000,
            'backupCount': 3,
        },
        'db-file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + '/db.log',
            'formatter': 'verbose',
            'maxBytes': 10000,
            'backupCount': 3,
        },
        'django-file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + '/django.log',
            'formatter': 'verbose',
            'maxBytes': 10000,
            'backupCount': 3,
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django-file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'apps': {
            'handlers': ['apps-file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # 'django.db.backends': {
        #     'handlers': ['db-file'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
    },
}

# Django Rest Framwork Config
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        '{{cookiecutter.project_slug}}.auth.authentication.UserJWTAuthentication',
    ),

    'EXCEPTION_HANDLER': 'base.exceptions.handler.custom_exception_handler',

    'DEFAULT_PAGINATION_CLASS': 'base.pagination.StandardPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'DEFAULT_THROTTLE_CLASSES': [
        'base.throttling.CloudflareScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'send_email': '1/min',
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

