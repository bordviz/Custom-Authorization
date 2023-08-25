from utils.unitofwork import IUnitOfWork
from schemas.auth import AuthRegister, AuthLogin
from schemas.user import UserCreate
from schemas.token import TokenRefresh, TokenData
from auth.auth import bcrypt_context, create_access_token, decode_token
from fastapi.exceptions import HTTPException
from models.user import User
from datetime import timedelta
from config import SECRET, REFRESH_SECRET, ALGORITHM

class AuthService:
    async def register(self, uow: IUnitOfWork, data: AuthRegister):
        user_model = UserCreate(
            first_name=data.first_name,
            last_name=data.last_name,
            username=data.username,
            email=data.email,
            hashed_password=bcrypt_context.hash(data.password)
        )
        async with uow:
            email_checker = await uow.user.get_one(email=data.email)
            username_checker = await uow.user.get_one(username=data.username)
            if email_checker:
                await uow.rollback()
                raise HTTPException(status_code=400, detail='A user with this email address is already registered')
            if username_checker:
                await uow.rollback()
                raise HTTPException(status_code=400, detail='A user with this username has already been registered')
            user_id = await uow.user.add_one(user_model.model_dump())
            await uow.commit()
            return user_id
        
    async def login(self, uow: IUnitOfWork, data: AuthLogin):
        async with uow:
            user: User = await uow.user.get_one(email= data.email, full_model=True)
            if not user:
                raise HTTPException(status_code=400, detail='Invalid password or email')
            if not bcrypt_context.verify(data.password, user.hashed_password):
                raise HTTPException(status_code=400, detail='Invalid password or email')
            token = create_access_token(username=user.username, user_id=user.id, secret=SECRET, expires_delta=timedelta(minutes=60))
            refresh_token = create_access_token(username=user.username, user_id=user.id, secret=REFRESH_SECRET, expires_delta=timedelta(days=3))
            return token, refresh_token
        
    async def refresh_token(self, uow: IUnitOfWork, data: TokenRefresh):
        if data.token_type.lower() != 'bearer':
            raise HTTPException(status_code=400, detail='Invalid token type')
        async with uow:
            try:
                token_data: TokenData = decode_token(data.refresh_token, REFRESH_SECRET, ALGORITHM)
                user = await uow.user.get_one(id=token_data.id, username=token_data.sub)
                token = create_access_token(username=user.username, user_id=user.id, secret=SECRET, expires_delta=timedelta(minutes=60))
                refresh_token = create_access_token(username=user.username, user_id=user.id, secret=REFRESH_SECRET, expires_delta=timedelta(days=3))
                return token, refresh_token
            except Exception:
                raise HTTPException(status_code=400, detail='Invalid token')
