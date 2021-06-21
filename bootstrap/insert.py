import logging
from database_engine import Base, engine

LOGGER = logging.getLogger()

LOGGER.info('bootstrapping db')

Base.metadata.create_all(engine)

LOGGER.info('finished boostrapping')