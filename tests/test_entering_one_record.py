import pytest
import logging

from database_engine import Base, Session, engine
from data_model.reloading_db_model import Contributor, Caliber, Load
from utils.reloading_functions import get_one_loads_by_email

LOGGER = logging.getLogger()


@pytest.mark.skip('we should do this once.  this will wipe out all the data, becareful')
def test_insert_one_record(boot_strap):
    session = Session()
    try:
        # first load
        contributor = Contributor('Roberto Torres', 'rtorres1228@yahoo.com')
        caliber = Caliber('45 acp')
        load = Load('strong load', 230, 'Tite Group', 4.3, 'CCI', 'P', 'S')
        contributor.calibers = [caliber]
        caliber.loads = [load]
        session.add(contributor)
        session.add(caliber)
        session.add(load)
        session.commit()

        # second load
        contributor = Contributor('Roberto Torres', 'rtorres1228@yahoo.com')
        caliber = Caliber('45 acp')
        load = Load('strong load', 230, 'Tite Group', 3.8, 'Win', 'P', 'S')
        contributor.calibers = [caliber]
        caliber.loads = [load]
        session.add(contributor)
        session.add(caliber)
        session.add(load)

        session.commit()
        session.close()
        assert True
    except Exception as e:
        assert False, 'error: {}'.format(str(e))
