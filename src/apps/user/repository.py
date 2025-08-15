from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.user.models import User
from src.core.repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(
            session=session,
            model=User,
        )

    async def get_users(self):
        statement = select(User.id)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def get_user_language_code(self, user_id: int) -> str:
        statement = select(User.language_code).where(User.id == user_id)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def get_admin_ids(self):
        statement = select(User.id).where(User.is_admin)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def get_user_ids_by_city(self, city: str):
        statement = select(User.id).where(User.city == city)
        result = await self.session.execute(statement)
        return result.scalars().all()