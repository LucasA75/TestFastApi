from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    if(exc.status_code == 404):
        exc.detail = f"{exc.detail}, try another URL or view the docs 🐔"
    return JSONResponse({"errors": [exc.detail],"status_code": exc.status_code}, status_code=exc.status_code)