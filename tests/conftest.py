import time
import pytest
import logging
from database_engine import Base, engine

LOGGER = logging.getLogger()


@pytest.fixture
def boot_strap():
    LOGGER.info('dropping all schema')
    Base.metadata.drop_all(engine)
    LOGGER.info('finished dropping all schema')
    time.sleep(3)
    LOGGER.info('bootstraping the schema')
    Base.metadata.create_all(engine)
    LOGGER.info('finished bootstrapping the schema')


