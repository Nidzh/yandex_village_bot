from sqlalchemy.orm import Mapped, mapped_column

from src.core.model import Base, bigint


class User(Base, Base.TimestampsMixin, Base.IsDeletedMixin):
    __tablename__ = "user"

    id: Mapped[bigint] = mapped_column(primary_key=True, index=True, unique=True, comment="ID Telegram")
    first_name: Mapped[str] = mapped_column(comment="First name")
    last_name: Mapped[str | None] = mapped_column(comment="Last name")
    username: Mapped[str | None] = mapped_column(comment="Username")
    language_code: Mapped[str | None] = mapped_column(comment="Language code")
    is_admin: Mapped[bool] = mapped_column(default=False, index=True, comment="Is admin")
    city: Mapped[str | None] = mapped_column(comment="City")