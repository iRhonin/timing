from sqlalchemy.orm import sessionmaker

from timing import settings
from timing.db.engine import engine


Session = sessionmaker(
    bind=engine,
    **settings.SQLALCHEMY['sessionmaker']
)
