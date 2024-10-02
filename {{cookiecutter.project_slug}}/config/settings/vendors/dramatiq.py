{% if cookiecutter.use_dramatiq == 'y' -%}
from ..base import env

DRAMATIQ_BROKER = {
    'BROKER': 'dramatiq.brokers.redis.RedisBroker',
    "OPTIONS": {
        'url': f'redis://:{env("REDIS_PASS")}@{env("REDIS_HOST")}:{env("REDIS_PORT")}/{env("REDIS_DB_TASK_QUEUE")}',
    },
    "MIDDLEWARE": [
        # "dramatiq.middleware.Prometheus",
        "dramatiq.middleware.AgeLimit",
        "dramatiq.middleware.TimeLimit",
        "dramatiq.middleware.Callbacks",
        "dramatiq.middleware.Retries",
        "django_dramatiq.middleware.DbConnectionsMiddleware",
        "django_dramatiq.middleware.AdminMiddleware",
    ]
}

DRAMATIQ_RESULT_BACKEND = {
    'BACKEND': 'dramatiq.results.backends.redis.RedisBackend',
    'BACKEND_OPTIONS': {
        'url': f'redis://:{env("REDIS_PASS")}@{env("REDIS_HOST")}:{env("REDIS_PORT")}/{env("REDIS_DB_TASK_QUEUE")}',
    },
    'MIDDLEWARE_OPTIONS': {
        'result_ttl': 60000
    }
}

# Defines which database should be used to persist Task objects when the
# AdminMiddleware is enabled.  The default value is "default".
DRAMATIQ_TASKS_DATABASE = "default"

DRAMATIQ_ADMIN_IGNORE_TASKS = []
DRAMATIQ_ADMIN_IGNORE_QUEUES = ['products', 'metrics']
{%- endif %}
