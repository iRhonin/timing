MYSQL = {
    'engine': 'mysql',
    'pool_size': 100,
    'debug': False,
    'username': 'mysql',
    'password': 'mysql',
    'host': 'mysql',
    'port': 5432,
    'db_name': 'timing',
}

SQLALCHEMY = {
    'debug': False,
    'sessionmaker': {
        'autoflush': False,
        'autocommit': False,
        'expire_on_commit': True,
        'twophase': False,
    }
}
