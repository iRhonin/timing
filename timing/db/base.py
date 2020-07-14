from sqlalchemy.ext.declarative import declarative_base

from .engine import metadata


class BaseModel(object):

    def to_dict(self):
        raise NotImplementedError()


DeclarativeBase = declarative_base(cls=BaseModel, metadata=metadata)
