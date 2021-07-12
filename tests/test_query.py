import pytest
import logging
import atexit

from database_engine import Base, Session, engine
from data_model.reloading_db_model import Contributor, Caliber, Load
from sqlalchemy.orm import Query


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
    assert loads

    LOGGER.info('loads:')
    for load in loads:
        LOGGER.info(f'name: {load.caliber_id}')

    SESSION.commit()


# @pytest.mark.skip('skip')
def test_get_loads_for_caliber():
    loads_for_caliber = SESSION.query(Caliber, Load).join(Load, Caliber.loads).all()
    SESSION.commit()
    assert loads_for_caliber

    for load in loads_for_caliber:
        caliber, load = load
        LOGGER.info(f'{caliber.caliber_name}, {load.load_name}')


def test_get_all_records():
    contributor_data = SESSION.query(Contributor, Caliber, Load).join(Caliber, Contributor.calibers).\
        join(Load, Caliber.loads).all()

    result = result_dict(contributor_data)

    assert len(result) > 0
    LOGGER.info(f'{result}')


def get_dict(rs):
    ret_dict = {}
    for obj in rs:
        ret_dict.update(clean_dict(obj.__dict__))
    return ret_dict


def result_dict(rs):
    return list(map(get_dict, rs))


def clean_dict(m_dict):
    del m_dict['_sa_instance_state']
    return m_dict

# todo: filter records by email, caliber, bullet weight



