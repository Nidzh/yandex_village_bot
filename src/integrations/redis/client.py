import functools

import redis
from redis.asyncio import BlockingConnectionPool, Redis

from src.core.settings import settings

redis_client = Redis.from_pool(
    BlockingConnectionPool.from_url(
        settings.redis.URL,
        max_connections=1000,
        timeout=10,
        health_check_interval=5,
        socket_connect_timeout=5,
        socket_keepalive=True,
        retry_on_timeout=True,
    )
)


def distributed_lock(key: str, timeout_seconds: int = 60):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                async with redis_client.lock(key, timeout=timeout_seconds, blocking=False):
                    return await func(*args, **kwargs)
            except redis.exceptions.LockError:
                pass

        return wrapper

    return decorator
