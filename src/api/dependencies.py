from utils.unitofwork import IUnitOfWork, UnitOfWork
from fastapi import Depends
from typing import Annotated
from schemas.user import UserRead
from auth.auth import get_current_user

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
CurrentUser = Annotated[UserRead, Depends(get_current_user)]