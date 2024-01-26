from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    email: str
    bio: str = ""
    image: Optional[str] = None