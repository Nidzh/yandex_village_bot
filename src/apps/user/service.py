from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.user.repository import UserRepository
from src.apps.user.schemas import UserCreate, UserUpdateSchema, UserSchema


class UserService:
    def __init__(self, session: AsyncSession = None):
        self.repo = UserRepository(session=session)

    async def create_user(self, user: UserCreate):
        await self.repo.create(user.model_dump())

    async def update_user(self, user: UserUpdateSchema):
        await self.repo.update(user.id, user.model_dump(exclude_none=True, exclude_unset=True, exclude={"id"}))

    async def create_or_update_user(self, user: UserCreate):
        existing_user = await self.repo.get_by_id(user.id)
        if existing_user:
            await self.repo.update(user.id, user.model_dump(exclude_none=True, exclude_unset=True))
        else:
            await self.repo.create(user.model_dump())

    async def get_users(self):
        return await self.repo.get_users()

    async def get_admin_ids(self):
        return await self.repo.get_admin_ids()

    async def get_user_language_code(self, user_id: int) -> str:
        return await self.repo.get_user_language_code(user_id=user_id)

    async def get_user_by_id(self, user_id: int) -> UserSchema:
        user_data = await self.repo.get_by_id(user_id)
        return UserSchema.model_validate(user_data)
