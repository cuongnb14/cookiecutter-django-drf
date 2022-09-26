from ..base import BASE_DIR, APPS_DIR

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR('staticfiles'))
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
