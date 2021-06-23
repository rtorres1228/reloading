import pytest
import logging

from database_engine import Base, Session, engine
from data_model.reloading_db_model import Contributor, Caliber, Load
from sqlalchemy.orm import Query

# test = Query()
# test.column_descriptions
LOGGER = logging.getLogger()


def test_get_contributors():
    session = Session()
    contributors = session.query(Contributor).all()
    assert contributors, 'nothing was returned'

    LOGGER.info('\n### All contributor:')
    for contributor in contributors:
        LOGGER.info(f'name: {contributor.name}, email: {contributor.email}')

    session.commit()
    session.close()


def test_get_calibers():
    session = Session()
    calibers = session.query(Caliber).all()

    assert calibers, 'nothing was returned'

    LOGGER.info('\n### calibers:')
    for caliber in calibers:
        LOGGER.info(f'name: {caliber.caliber_name}')

    session.commit()
    session.close()


def test_get_loads():
    session = Session()
    loads = session.query(Load).all()

    LOGGER.info('loads:')
    for load in loads:
        LOGGER.info(f'name: {load.caliber_id}')

    session.commit()
    session.close()


# @pytest.mark.skip('skip')
def test_get_loads_for_caliber():
    session = Session()
    loads_for_caliber = session.query(Caliber, Load).join(Load, Caliber.loads).all()

    assert loads_for_caliber

    for load in loads_for_caliber:
        caliber, load = load
        LOGGER.info(f'{caliber.caliber_name}, {load.load_name}')

    session.commit()
    session.close()
