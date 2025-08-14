from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, ConfigDict


class CustomBaseModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    def serializable_dict(self, **kwargs):
        """Return a dict which contains only serializable fields."""
        default_dict = self.model_dump()
        return jsonable_encoder(default_dict)
