from src.core.settings import settings
from src.db.manager import DatabaseSessionManager

session_kwargs = {"autocommit": False, "autoflush": True, "expire_on_commit": True}

engine_kwargs = {
    "echo": settings.config.DEBUG,
    "echo_pool": False,
    "pool_size": 5,  # The number of connections to keep open inside the connection pool.
    "max_overflow": 0,  # The number of connections to allow in connection pool "overflow", that is connections that can be opened above and beyond the pool_size setting, which defaults to five.
    "pool_timeout": 60,  # The number of seconds to wait before giving up on getting a connection from the pool.
    "pool_recycle": 1200,  # This setting causes the pool to recycle connections after the given number of seconds has passed. It defaults to -1, or no timeout. For example, setting to 3600 means connections will be recycled after one hour.
    "pool_pre_ping": True,  # If True will enable the connection pool "pre-ping" feature that tests connections for liveness upon each checkout.
}


sessionmanager = DatabaseSessionManager(settings.postgresql.URL, engine_kwargs, session_kwargs)


async def get_session():
    async with sessionmanager.session() as session:
        yield session


async def get_connect():
    async with sessionmanager.connect() as connect:
        yield connect
