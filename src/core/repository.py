import json
from typing import Generic, TypeVar
from uuid import UUID

import httpx
from loguru import logger
from fastapi_filter.contrib.sqlalchemy import Filter
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import inspect, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import DeclarativeBase

T = TypeVar("T", bound=DeclarativeBase)


class BaseApiRepository:
    def __init__(self, base_url: str = "", auth=None, ssl_verify=True):
        self.base_url = base_url
        self.auth = auth
        self.ssl_verify = ssl_verify

    async def request(self, method: str, endpoint: str, **kwargs):
        async with httpx.AsyncClient(auth=self.auth, verify=self.ssl_verify) as client:
            response = await client.request(method, f"{self.base_url}{endpoint}", **kwargs)
            response.raise_for_status()
            return response.json()


class BaseRepository(Generic[T]):
    def __init__(self, session: AsyncSession, model: type[T]):
        """
        Инициализирует репозиторий с указанием модели.
        :param model: Класс модели SQLAlchemy, связанный с таблицей в базе данных.
        """
        self.session = session
        self.model = model

    async def get_by_id(self, id, with_deleted: bool = False) -> T | None:
        """
        Получает объект по его ID, используя предоставленную сессию.
        :param with_deleted: Получать удаленные объекты
        :param id: ID объекта для поиска.
        :return: Экземпляр модели или None, если объект не найден.
        """
        statement = select(self.model).where(self.model.id == id)

        if with_deleted and "is_deleted" in inspect(self.model).attrs:
            statement = statement.where(self.model.is_deleted == False)

        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def get_by_uuid(self, uuid: UUID, with_deleted: bool = False) -> T | None:
        """
        Получает объект по его ID, используя предоставленную сессию.
        :param with_deleted: Получать удаленные объекты
        :param uuid: ID объекта для поиска.
        :return: Экземпляр модели или None, если объект не найден.
        """
        statement = select(self.model).where(self.model.uuid == uuid)

        if with_deleted and "is_deleted" in inspect(self.model).attrs:
            statement = statement.where(self.model.is_deleted == False)

        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def get_all(self, filters: Filter = None, use_pagination: bool = True, with_deleted: bool = False):
        """
        Получает все объекты модели с пагинацией, используя предоставленную сессию.
        param use_pagination: Флаг использования пагинации.
        :return: Список объектов модели.
        """
        statement = select(self.model)
        if with_deleted and "is_deleted" in inspect(self.model).attrs:
            statement = statement.where(self.model.is_deleted == False)
        if filters:
            statement = filters.filter(statement)
            statement = filters.sort(statement)
        if use_pagination:
            return await paginate(self.session, statement)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def get_by_filters(self, use_pagination: bool = True, **filters):
        """
        Получает все объекты модели по указанным фильтрам.
        param use_pagination: Флаг использования пагинации.
        :return: Список объектов модели.
        """
        statement = select(self.model).filter_by(**filters)
        if use_pagination:
            return await paginate(self.session, statement)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def create(self, data: dict, use_commit: bool = True) -> T:
        """
        Создает новый объект модели с данными из словаря.
        :param data: Словарь с данными для нового объекта.
        :param use_commit: Использование commit.
        :return: Созданный объект модели.
        """
        new_object = self.model(**data)
        self.session.add(new_object)
        if use_commit:
            await self.session.commit()
            await self.session.refresh(new_object)
        else:
            await self.session.flush()
        return new_object

    async def update(self, id: int, data: dict):
        """
        Обновляет объект по его ID данными из словаря.
        :param id: ID объекта для обновления.
        :param data: Словарь с обновленными данными.
        :return: Обновленный объект модели или None, если объект не найден.
        """
        statement = select(self.model).where(self.model.id == id)
        if "is_deleted" in inspect(self.model).attrs:
            statement = statement.where(self.model.is_deleted == False)
        result = await self.session.execute(statement)
        existing_object = result.scalar_one_or_none()
        if existing_object:
            for key, value in data.items():
                setattr(existing_object, key, value)
            await self.session.commit()
            await self.session.refresh(existing_object)
            return existing_object
        return None

    async def update_by_id(self, id: UUID, data: dict):
        """Перезапись объекта по id при гарантированном наличии объекта."""
        statement = (
            update(self.model)
            .where(
                self.model.id == id,
            )
            .values(**data)
        )
        await self.session.execute(statement)
        await self.session.commit()

    async def update_by_uuid(self, uuid: UUID, data: dict):
        """Перезапись объекта по id при гарантированном наличии объекта."""
        statement = (
            update(self.model)
            .where(
                self.model.uuid == uuid,
            )
            .values(**data)
        )
        await self.session.execute(statement)
        await self.session.commit()

    async def delete(self, id: UUID) -> bool:
        """
        Удаляет объект по его ID.
        :param id: ID объекта для удаления.
        :return: True, если объект был удален, иначе False.
        """
        statement = select(self.model).where(self.model.id == id)
        if "is_deleted" in inspect(self.model).attrs:
            statement = statement.where(self.model.is_deleted == False)
        result = await self.session.execute(statement)
        object_to_delete = result.scalar_one_or_none()
        if object_to_delete:
            await self.session.delete(object_to_delete)
            await self.session.commit()
            return True
        return False

    async def soft_delete(self, id: UUID) -> bool:
        """
        Выполняет "мягкое удаление" объекта, устанавливая флаг is_deleted в True.
        :param id: ID объекта для "мягкого удаления".
        :return: True, если флаг успешно установлен, иначе False.
        """
        statement = select(self.model).where(self.model.id == id)
        if "is_deleted" in inspect(self.model).attrs:
            statement = statement.where(self.model.is_deleted == False)
        result = await self.session.execute(statement)
        object_to_soft_delete = result.scalar_one_or_none()
        if object_to_soft_delete:
            object_to_soft_delete.is_deleted = True
            await self.session.commit()
            return True
        return False

    async def create_many(self, data_list: list[dict], use_commit: bool = True) -> list[T]:
        """
        Создает несколько новых объектов модели с данными из списка словарей.
        :param data_list: Список словарей с данными для новых объектов.
        :param use_commit: Использование commit.
        :return: Список созданных объектов модели.
        """
        new_objects = [self.model(**data) for data in data_list]
        self.session.add_all(new_objects)
        if use_commit:
            await self.session.commit()
            for obj in new_objects:
                await self.session.refresh(obj)
        else:
            await self.session.flush()
        return new_objects
