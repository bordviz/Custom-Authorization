from utils.unitofwork import IUnitOfWork
from fastapi import HTTPException

class UserService:
    async def get_user_by_id(self, uow: IUnitOfWork, user_id: int):
        async with uow:
            user = await uow.user.get_one(id=user_id)
            if not user:
                raise HTTPException(status_code=404, detail='User not found')
            return user

    async def get_all_users(self, uow: IUnitOfWork):
        async with uow:
            users = await uow.user.get_all()
            if users == []:
                raise HTTPException(status_code=404, detail='Users not found')
            return users