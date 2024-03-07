REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        '{{cookiecutter.project_slug}}.auth.authentication.UserJWTAuthentication',
    ),

    'EXCEPTION_HANDLER': 'common.exceptions.handler.custom_exception_handler',

    'DEFAULT_PAGINATION_CLASS': 'common.pagination.StandardPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'DEFAULT_THROTTLE_CLASSES': [
        'common.throttling.CloudflareScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'send_email': '1/min',
    }
}
