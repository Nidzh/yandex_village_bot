from datetime import datetime
from typing import Annotated

from sqlalchemy import BIGINT, JSON, SMALLINT, TEXT, func
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

smallint = Annotated[int, "smallint"]
bigint = Annotated[int, "bigint"]


class Base(DeclarativeBase):
    """Base parent model for all SQLAlchemy models."""

    type_annotation_map = {
        list[str]: ARRAY(TEXT),
        str: TEXT,
        datetime: TIMESTAMP(timezone=True),
        JSON: JSONB,
        smallint: SMALLINT,
        bigint: BIGINT,
    }

    class TimestampsMixin:
        @declared_attr
        def created_at(cls) -> Mapped[datetime]:
            return mapped_column(
                default=func.now(),
                nullable=False,
                comment="Временная метка создания записи",
            )

        @declared_attr
        def updated_at(cls) -> Mapped[datetime]:
            return mapped_column(default=func.now(), onupdate=func.now(), comment="Временная метка последнего обновления записи")

    class IsDeletedMixin:
        @declared_attr
        def is_deleted(cls) -> Mapped[bool]:
            return mapped_column(default=False, comment="Признак удаления")
