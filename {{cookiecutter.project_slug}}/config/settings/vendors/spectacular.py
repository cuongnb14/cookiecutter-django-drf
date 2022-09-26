from ..base import env

SPECTACULAR_SETTINGS = {
    'TITLE': '{{cookiecutter.project_name}} API',
    'DESCRIPTION': '{{cookiecutter.project_name}} API document',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX': '/v1',
    'SERVERS': [{'url': env('SPECTACULAR_SETTINGS_SERVER_URL')}],
    'SCHEMA_PATH_PREFIX_TRIM': True,
    'CONTACT': {
        'name': 'Developer',
        'email': 'demo@demo.com'
    },
    'POSTPROCESSING_HOOKS': [
        'config.schema.custom_postprocessing_hook'
    ],
    'EXTENSIONS_ROOT': {
        'x-tagGroups': [
            {
                'name': 'User',
                'tags': ['auth', 'account', 'users']
            }
        ]
    }
}
