from pydantic import BaseModel, EmailStr
from datetime import datetime


class ClientCreate(BaseModel):
    name: str
    contact_email: EmailStr | None = None


class ClientRead(BaseModel):
    id: int
    name: str
    email: str | None
    created_at: datetime

    class Config:
        from_attributes = True