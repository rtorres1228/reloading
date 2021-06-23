import pytest
import logging
import atexit

from database_engine import Base, Session, engine
from data_model.reloading_db_model import Contributor, Caliber, Load
from sqlalchemy.orm import Query

# test = Query()
# test.column_descriptions
LOGGER = logging.getLogger()

SESSION = Session()
atexit.register(SESSION.close)

def test_get_contributors():
    contributors = SESSION.query(Contributor).all()
    assert contributors, 'nothing was returned'

    LOGGER.info('\n### All contributor:')
    for contributor in contributors:
        LOGGER.info(f'name: {contributor.name}, email: {contributor.email}')

    SESSION.commit()


def test_get_calibers():
    calibers = SESSION.query(Caliber).all()

    assert calibers, 'nothing was returned'

    LOGGER.info('\n### calibers:')
    for caliber in calibers:
        LOGGER.info(f'name: {caliber.caliber_name}')

    SESSION.commit()


def test_get_loads():
    loads = SESSION.query(Load).all()

    LOGGER.info('loads:')
    for load in loads:
        LOGGER.info(f'name: {load.caliber_id}')

    SESSION.commit()


# @pytest.mark.skip('skip')
def test_get_loads_for_caliber():
    loads_for_caliber = SESSION.query(Caliber, Load).join(Load, Caliber.loads).all()

    assert loads_for_caliber

    for load in loads_for_caliber:
        caliber, load = load
        LOGGER.info(f'{caliber.caliber_name}, {load.load_name}')

    SESSION.commit()

