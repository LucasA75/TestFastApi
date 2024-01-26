from fastapi import FastAPI
from routes.api import router as api_router
from starlette.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from routes.errors.error import http_error_handler

def get_application() -> FastAPI:
    application = FastAPI()
    
    application.add_middleware(CORSMiddleware)
    
    application.add_exception_handler(HTTPException, http_error_handler)
    
    application.include_router(api_router)
    
    
    return application

app = get_application()



""" 
Para correr el codigo se ejecuta:
uvicorn main:app --reload 
Why?
main: the file main.py (the Python "module").
app: the object created inside of main.py with the line app = FastAPI().
--reload: make the server restart after code changes. Only do this for development.

"""

