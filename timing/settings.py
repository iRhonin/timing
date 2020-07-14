MYSQL = dict(
    engine='mysql',
    pool_size=100,
    debug=False,
    username='timing',
    password='timing',
    host='127.0.0.1',
    port=3306,
    db_name='timing',
)

SQLALCHEMY = dict(
    debug=False,
    sessionmaker=dict(
        autoflush=False,
        autocommit=False,
        expire_on_commit=True,
        twophase=False,
    ),
)

JWT = dict(
    secret='change-me',
    maxage=2678400,  # 30 Days
    algorithm='HS256',
)
