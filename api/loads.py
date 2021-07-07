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


@loads_api.route('/all')
def get_all_records():
    session = Session()
    contributor_data = session.query(Contributor).join(Caliber, Contributor.calibers).join(Load, Caliber.loads).all()
    caliber_data = session.query(Load).join(Load, Caliber.loads).join(Load, Caliber.loads).all()
    load_data = session.query(Caliber).join(Load, Caliber.loads).join(Load, Caliber.loads).all()

    contributors = result_dicts(contributor_data)
    calibers = result_dicts(caliber_data)
    loads = result_dicts(load_data)
    result = [*contributors, *calibers, *loads]
    assert len(result) > 0
    LOGGER.info(f'{result}')
    return jsonify(f'{result}')


def result_dict(r):
    ret_dict = {}
    ret_dict.update(clean_dict(r.__dict__))
    return ret_dict


def result_dicts(rs):
    return list(map(result_dict, rs))


def clean_dict(m_dict):
    del m_dict['_sa_instance_state']
    return m_dict
