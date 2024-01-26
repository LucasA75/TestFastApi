from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from resources import string
from models.schemas.users import (
    UserTest,
    UserInLogin,
    UserInResponse,
    UserWithToken,
)

from resources import string

router = APIRouter()


@router.post("", response_model=UserTest, name="auth:login")
async def login(user: UserTest) -> str:
    
    wrong_login_error = HTTPException(
        status_code=HTTP_400_BAD_REQUEST,
        detail=string.INCORRECT_LOGIN_INPUT,
    )

    raise wrong_login_error 

