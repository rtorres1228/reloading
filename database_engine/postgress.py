from sqlalchemy import create_engine

USER = 'rtorres1228'
PASSWORD = 'Welcome1!'


def get_database_engine():
    params = {
                'pool_size': 10,
                'max_overflow': 2,
                'pool_recycle': 10,
                'pool_timeout': 10
    }
    engine = create_engine('postgresql://{0}:{1}@localhost:5432/sqlalchemy'.format(USER, PASSWORD), **params)
    return engine
