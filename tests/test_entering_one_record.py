import pytest
import logging

from database_engine import Base, Session, engine
from data_model.reloading_db_model import Contributor, Caliber, Load
from utils.reloading_functions import get_one_loads_by_email

LOGGER = logging.getLogger()


def test_insert_one_record(boot_strap):
    session = Session()
    try:
        contributor = Contributor('Roberto Torres', 'rtorres1228@yahoo.com')
        caliber = Caliber('45 acp')
        load = Load('mild load', 'Tite Group', 4.3, 'CCI', 'SM Pistol')

        session.add(contributor)
        session.add(caliber)
        session.add(load)

        session.commit()
        session.close()
        assert True
    except Exception as e:
        assert False, 'error: {}'.format(str(e))

def test_get_load_by_email():
    assert get_one_loads_by_email('rtorres1228@yaoho.com'), 'could not get record'