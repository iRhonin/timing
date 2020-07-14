from sqlalchemy import Integer, Column, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from timing.db.base import DeclarativeBase


DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'


class Time(DeclarativeBase):
    __tablename__ = 'times'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    hours = Column(Integer, nullable=False)

    user = relationship(
        'User',
        foreign_keys=user_id,
        uselist=False,
        back_populates='times',
    )

    def to_dict(self):
        return dict(
            id=self.id,
            hours=self.hours,
            createdAt=self.created_at.strftime(DATETIME_FORMAT),
        )
