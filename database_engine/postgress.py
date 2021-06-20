from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = 'usr'
PASSWORD = 'pass!'


params = {
            'pool_size': 10,
            'max_overflow': 2,
            'pool_recycle': 10,
            'pool_timeout': 10
}

engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)
Base = declarative_base()
