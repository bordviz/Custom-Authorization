from datetime import datetime
from db.db import Base
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from schemas.user import UserRead

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, primary_key=True, index=True)
    email = Column(String, nullable=False, primary_key=True, index=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)

    def to_read_model(self) -> UserRead:
        return UserRead(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            email=self.email,
            created_at=self.created_at
        )