from .auth import router as router_auth
from .user import router as router_user
from fastapi import APIRouter

all_routers = [
    router_auth,
    router_user
]
