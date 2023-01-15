{% if cookiecutter.use_celery == 'y' -%}
# Celery
# ------------------------------------------------------------------------------
CELERY_TIMEZONE = 'UTC'

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
