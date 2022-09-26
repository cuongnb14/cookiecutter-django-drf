from ..base import env, INSTALLED_APPS

if env.bool('ENABLE_DJANGO_EXTENSIONS'):
    INSTALLED_APPS += ["django_extensions"]  # noqa F405
