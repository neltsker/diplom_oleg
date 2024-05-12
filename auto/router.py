from fastapi import APIRouter, Response, status
from starlette.requests import Request
from .models import *

user_router = APIRouter(prefix="/users", tags=["auth"])


@user_router.get("/")
async def index(request: Request):
    return "hi from user api Router"