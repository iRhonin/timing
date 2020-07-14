from sqlalchemy.orm import sessionmaker, scoped_session

from timing import settings
from timing.db.engine import engine


session_factory = sessionmaker(
    bind=engine,
    **settings.SQLALCHEMY['sessionmaker']
)
Session = scoped_session(session_factory)
