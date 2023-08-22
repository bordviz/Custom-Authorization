from fastapi import APIRouter
from schemas.auth import AuthRegister, AuthLogin
from .dependencies import UOWDep
from services.auth import AuthService
from schemas.token import TokenCreate, TokenRefresh

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post('/register', status_code=201)
async def register(
    data: AuthRegister,
    uow: UOWDep
):
    print(data.model_dump())
    user_id = await AuthService().register(uow, data)
    return {'status': 'success', 'detail': f'User with id {user_id} successfully create'}

@router.post('/login', status_code=200, response_model=TokenCreate)
async def login(
    data: AuthLogin,
    uow: UOWDep
):
    token, refresh_token = await AuthService().login(uow, data)
    return TokenCreate(access_token=token, refresh_token=refresh_token, token_type='bearer')

@router.post('/refresh-token', status_code=200, response_model=TokenCreate)
async def refresh_token(
    data: TokenRefresh,
    uow: UOWDep
):
    token, refresh_token = await AuthService().refresh_token(uow, data)
    return TokenCreate(access_token=token, refresh_token=refresh_token, token_type='bearer')
