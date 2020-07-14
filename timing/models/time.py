from sqlalchemy import Integer, Unicode, Column, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from timing.db.base import DeclarativeBase


class Time(DeclarativeBase):
    __tablename__ = 'times'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    hours = Column(Integer, nullable=False)

    user = relationship('User', foreign_keys=user_id, uselist=False)

    def to_dict(self):
        return dict(
            id=self.id,
            hours=self.hours,
            createdAt=self.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
        )
