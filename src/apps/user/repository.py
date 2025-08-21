from sqlalchemy import select, func, update
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

    async def create_answer(self, data: dict):
        from src.apps.user.models import Answer
        new_object = Answer(**data)
        self.session.add(new_object)
        await self.session.commit()

    async def pop_wardrobe_ticket(self) -> int:
        from src.apps.user.models import WardrobeTicket
        pick = (
            select(WardrobeTicket.ticket)
            .where(WardrobeTicket.is_used.is_(False))
            .order_by(func.random())
            .limit(1)
            .with_for_update(skip_locked=True)
        ).cte("pick")

        # Важно: select(...) в WHERE нужно завернуть в scalar_subquery()
        ticket = await self.session.scalar(
            update(WardrobeTicket)
            .where(WardrobeTicket.ticket == select(pick.c.ticket).scalar_subquery())
            .values(is_used=True)
            .returning(WardrobeTicket.ticket)
        )

        if ticket is None:
            raise ValueError("No free wardrobe tickets available")

        return ticket