from sqlalchemy import Integer, Unicode, Column
from sqlalchemy.orm import relationship

from timing.db.base import DeclarativeBase


class User(DeclarativeBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(10), nullable=False, unique=True, index=True)

    times = relationship(
        'Time',
        back_populates='user',
    )

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
        )
