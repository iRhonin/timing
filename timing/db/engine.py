from sqlalchemy import create_engine, MetaData

from timing import settings


engine = create_engine(
    '{engine}://{username}:{password}@{host}:{port}/{db_name}'.format(
        **settings.MYSQL
    ),
    pool_size=settings.MYSQL['pool_size'],
    echo=settings.SQLALCHEMY['debug']
)

metadata = MetaData(bind=engine)
