from ..base import env

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis://:{env("REDIS_PASSWORD")}@{env("REDIS_HOST")}:{env("REDIS_PORT")}/{env("REDIS_CACHE_DB")}',
    }
}
