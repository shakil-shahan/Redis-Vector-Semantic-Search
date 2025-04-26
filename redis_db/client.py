import redis
from config.settings import REDIS_CONFIG


def get_redis_client():
    return redis.Redis(**REDIS_CONFIG)
