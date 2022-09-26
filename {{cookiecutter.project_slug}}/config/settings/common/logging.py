from ..base import BASE_DIR
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
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        '{{cookiecutter.project_slug}}': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # 'django.db.backends': {
        #     'handlers': ['db-file'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
    },
}
