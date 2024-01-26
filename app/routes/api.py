from fastapi import APIRouter
from routes import users,items,login

router = APIRouter()

router.include_router(users.router, tags=["users"], prefix="/users")
router.include_router(items.router, tags=["items"], prefix="/items")
router.include_router(login.router, tags=["login"], prefix="/login")