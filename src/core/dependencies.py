from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.context import get_session


def get_service(service_class):
    async def _get_service(
        session: AsyncSession = Depends(get_session),
    ):
        return service_class(session=session)

    return Depends(_get_service)
