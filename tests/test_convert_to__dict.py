from io import SEEK_CUR
import pytest
import logging

from database_engine import Base, Session, engine
from api.utils.conver_to_dictionary import result_dict, get_dict
from data_model.reloading_db_model import Load, Contributor, Caliber

LOGGER = logging.getLogger()



@pytest.fixture(scope='module')
def setup_tests():
    SESSION = Session()
    yield SESSION
    SESSION.close()


def test_get_dict(setup_tests):
    session = setup_tests

    loads = session.query(Load).all()
    
    #for single table outputs just use get_dict
    result = get_dict(loads)
    session.commit()

    LOGGER.info('result: %s', result)

    assert len(result) > 0, 'no loads were found in the db'


def test_result_dict(setup_tests):
    session = setup_tests

    contributor_data = session.query(Contributor, Caliber, Load).join(Caliber, Contributor.calibers). \
        join(Load, Caliber.loads).all()
    
    #for single table outputs just use get_dict
    result = result_dict(contributor_data)
    session.commit()

    LOGGER.info('result: %s', result)

    assert len(result) > 0, 'no loads were found in the db'

