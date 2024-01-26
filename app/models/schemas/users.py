from typing import Optional
from pydantic import BaseModel, EmailStr, HttpUrl
from models.domain.users import User

class UserTest(User):
    id: int

class UserInLogin():
    email: EmailStr
    password: str


class UserInCreate(UserInLogin):
    username: str


class UserInUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[HttpUrl] = None


class UserWithToken(User):
    token: str


class UserInResponse():
    user: UserWithToken