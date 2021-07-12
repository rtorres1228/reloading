import atexit
import logging
from flask import jsonify, Blueprint
from database_engine import Base, Session, engine

from data_model.reloading_db_model import Contributor, Caliber, Load

LOGGER = logging.getLogger()
loads_api = Blueprint('loads_api', __name__)


'''getter functions'''


@loads_api.route('/contributors')
def get_contributors():
    return jsonify('hello')


@loads_api.route('/loads')
def get_loads():
    session = Session()
    atexit.register(session.close)

    loads = session.query(Load).all()
    assert loads

    LOGGER.info('loads:')
    for load in loads:
        LOGGER.info(f'name: {load.caliber_id}')

    session.commit()
    return jsonify(loads)

#todo: need to group results per contributor.  one contributor should be a dictionary which then contains a list of nodes
@loads_api.route('/all')
def get_all_records():
    session = Session()
    atexit.register(session.close)
    contributor_data = session.query(Contributor, Caliber, Load).join(Caliber, Contributor.calibers). \
        join(Load, Caliber.loads).all()

    result = result_dict(contributor_data)
    session.commit()
    assert len(result) > 0
    LOGGER.info(f'{result}')
    return jsonify(f'{result}')


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
