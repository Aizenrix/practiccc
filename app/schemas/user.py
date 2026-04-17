from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserOut(BaseModel):
    id: int
    email: str
    username: str
    phone: str
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
