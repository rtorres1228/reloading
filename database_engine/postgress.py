
import yaml

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open('./secrets/config.yml') as config:
    app_config = yaml.safe_load_all(config)
    for config_data in app_config:
        print(config_data)
        conn = config_data['postgresql']['conn_string']

params = {
            'pool_size': 10,
            'max_overflow': 2,
            'pool_recycle': 10,
            'pool_timeout': 10
}

engine = create_engine(conn, **params)
Session = sessionmaker(bind=engine)
Base = declarative_base()
