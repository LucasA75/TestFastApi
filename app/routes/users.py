from fastapi import APIRouter, Depends,HTTPException
from models.schemas.users import UserTest
from resources import string
from starlette import status

router = APIRouter()

@router.get("/{userID}", response_model=UserTest, name="users:get-current-user")
async def retrieve_current_user(userID : int) -> UserTest:
    return UserTest(id= userID,email="MailDePrueba@Gamil.com",username="Chamaquito2024")

@router.get("user/{userID}", response_model=UserTest)
async def retrieve_current_user(userID : int) -> UserTest:
    return UserTest(id= userID,email="MailDePrueba@Gamil.com",username="Chamaquito2024")

@router.post("/user",status_code= status.HTTP_201_CREATED)
async def retrieve_current_user(user: UserTest) -> str:
    print(user)
    if(user.id == 2):
        wrong_userCreation_error = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=string.WRONG_USER_CREATION,
    )   
        raise wrong_userCreation_error
        
    return "guardado en bbdd"