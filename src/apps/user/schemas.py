from datetime import datetime

from pydantic import Field

from src.core.schema import CustomBaseModel


class UserCreate(CustomBaseModel):
    id: int = Field(..., description="Telegram ID")
    first_name: str | None = Field(None, description="First name")
    last_name: str | None = Field(None, description="Last name")
    username: str | None = Field(None, description="Username")
    language_code: str | None = Field(None, description="Language code")


class UserUpdateSchema(UserCreate):
    city: str | None = Field(None, description="City")


class UserSchema(UserUpdateSchema):
    is_admin: bool = Field(..., description="Is admin")
    created_at: datetime = Field(..., description="Created at")
    updated_at: datetime = Field(..., description="Updated at")

