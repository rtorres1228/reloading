import pytest
import logging
import atexit
from sqlalchemy.orm import Query

from database_engine import Base, Session, engine
from data_model.reloading_db_model import Contributor, Caliber, Load
from sqlalchemy.orm import Query
from collections.abc import Iterable

# test.column_descriptions
LOGGER = logging.getLogger()

CALIBER = '45'
SESSION = Session()
atexit.register(SESSION.close)

Query


def test_get_contributors():
    contributors = SESSION.query(Contributor).all()
    assert contributors, 'nothing was returned'

    LOGGER.info('\n### All contributor:')
    for contributor in contributors:
        LOGGER.info(f'name: {contributor.name}, email: {contributor.email}')

    SESSION.commit()



# @pytest.mark.skip('skip')
def test_get_loads():
    loads_for_caliber = SESSION.query(Caliber, Load, Contributor).join(Caliber, Contributor.calibers).join(Load, Caliber.loads).all()
    SESSION.commit()
    assert loads_for_caliber

    for load in loads_for_caliber:
        caliber, load, contributor = load
        LOGGER.info(f'contributor: {contributor.email}, for caliber: {caliber.caliber_name}, load name: {load.load_name}, bullet weight: {load.bullet_weight}, powder brand: {load.powder_brand}, powder charge: {load.powder_charge}')

def test_get_load_for_caliber__using_like():
    caliber = '%{}%'.format(CALIBER)
    loads_for_caliber = SESSION.query(Caliber, Load, Contributor).join(Caliber, Contributor.calibers).filter(Caliber.caliber_name.like(caliber)).join(Load, Caliber.loads).all()
    assert loads_for_caliber
    for load in loads_for_caliber:
        caliber, load, contributor = load
        LOGGER.info(f'contributor: {contributor.email}, for caliber: {caliber.caliber_name}, load name: {load.load_name}, bullet weight: {load.bullet_weight}, powder brand: {load.powder_brand}, powder charge: {load.powder_charge}')
    SESSION.commit()

def test_get_all_records():
    contributor_data = SESSION.query(Contributor, Caliber, Load).join(Caliber, Contributor.calibers).\
        join(Load, Caliber.loads).all()

    result = result_dict(contributor_data)

    assert len(result) > 0
    LOGGER.info(f'{result}')


def test_get_all_records_per_contributor_email():
    query_filter = {'email': 'rtorres1228@yahoo.com'}
    contributor_data = SESSION.query(Contributor, Caliber, Load).filter_by(**query_filter).\
        join(Caliber, Contributor.calibers). \
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



