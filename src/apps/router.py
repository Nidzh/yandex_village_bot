from fastapi import APIRouter

from src.apps.user.api import router as _user_router

router = APIRouter()

router.include_router(_user_router, prefix="/user", tags=["User"])
