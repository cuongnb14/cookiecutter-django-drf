from ..base import env

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
