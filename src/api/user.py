from fastapi import APIRouter
from schemas.user import UserRead
from .dependencies import CurrentUser, UOWDep
from services.user import UserService
from typing import List

router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.get('/profile', status_code=200, response_model=UserRead)
async def get_user_profile(
    user: CurrentUser
):
    return user

@router.get('/all', status_code=200, response_model=List[UserRead])
async def get_all_users(
    uow: UOWDep
):
    users = await UserService().get_all_users(uow)
    return users

@router.get('{user_id}', status_code=200, response_model=UserRead)
async def get_user_by_id(
    user_id: int,
    uow: UOWDep
):
    user = await UserService().get_user_by_id(uow, user_id)
    return user