import json

from src.apps.user.service import UserService
from src.db.context import get_session


def load_media():
    """Load media from the JSON file."""
    with open('./media/media_map.json', 'r') as json_file:
        return json.load(json_file)


async def get_users():
    async for session in get_session():
        return await UserService(session=session).get_users()
    return None


async def get_admin_users():
    async for session in get_session():
        return await UserService(session=session).get_admin_ids()
    return None


async def get_moscow_users():
    async for session in get_session():
        return await UserService(session=session).get_user_ids_by_city(city="moscow")
    return None


async def get_belgrad_users():
    async for session in get_session():
        return await UserService(session=session).get_user_ids_by_city(city="belgrad")
    return None
