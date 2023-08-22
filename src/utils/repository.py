from abc import ABC, abstractmethod
from db.db import AsyncSession
from sqlalchemy import ColumnExpressionArgument, select, insert, and_
from sqlalchemy.exc import NoResultFound

class AbstractRepository(ABC):
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError
    
    @abstractmethod
    async def get_one(self):
        raise NotImplementedError
    
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError
    
class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__ (self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
    
    async def get_one(self, full_model: bool = False, **filter_by):
        try:
            stmt = select(self.model).filter_by(**filter_by).limit(1)
            print(stmt)
            res = await self.session.execute(stmt)
            res = res.scalar_one()
            if not full_model:
                res = res.to_read_model()
            return res
        except NoResultFound:
            return None
        
    async def add_one(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res_id = await self.session.execute(stmt)
        return res_id.scalar_one()