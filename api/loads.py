import atexit
import logging
from flask import jsonify, Blueprint, Flask
from collections.abc import Iterable

from api.utils.conver_to_dictionary import result_dict, get_dict
from database_engine import Base, Session, engine
from data_model.reloading_db_model import Contributor, Caliber, Load
from api.error_handling.errors import InvalidUsage


LOGGER = logging.getLogger()

app = Flask(__name__)
loads_api = Blueprint('loads_api', __name__)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


'''getter functions'''
@loads_api.route('/contributors/all')
def get_contributors():
    return jsonify('hello')


@loads_api.route('/loads/all')
def get_loads():
    session = Session()
    atexit.register(session.close)
    loads = session.query(Load).all()
    #for single table outputs just use get_dict
    result = get_dict(loads)
    session.commit()
    LOGGER.info('result: %s', result)
    if not len(result) > 0:
        raise InvalidUsage('no loads were found in the db')
    return jsonify(f'{result}')


@loads_api.route('/all')
def get_all_records():
    session = Session()
    atexit.register(session.close)
    contributor_data = session.query(Contributor, Caliber, Load).join(Caliber, Contributor.calibers). \
        join(Load, Caliber.loads).all()
    result = result_dict(contributor_data)
    session.commit()
    LOGGER.info(f'{result}')
    if not len(result) > 0:
        raise InvalidUsage('no loads were found please try again')
    return jsonify(f'{result}')

@loads_api.route('/email/<email>/all')
def get_all_records_email(email):
    session = Session()
    atexit.register(session.close)
    contributor_data = session.query(Contributor, Caliber, Load).filter_by(email=email).\
        join(Caliber, Contributor.calibers). \
        join(Load, Caliber.loads).all()
    result = result_dict(contributor_data)
    session.commit()
    LOGGER.info(f'{result}')
    if not len(result) > 0:
        raise InvalidUsage('no loads were found please try again')
    return jsonify(f'{result}')

@loads_api.route('/caliber/<caliber>/all')
def get_load__caliber(caliber):
    caliber = '%{}%'.format(caliber)
    session = Session()
    loads_for_caliber = session.query(Caliber, Load, Contributor).join(Caliber, Contributor.calibers).filter(Caliber.caliber_name.like(caliber)).join(Load, Caliber.loads).all()
    result = result_dict(loads_for_caliber)
    session.commit()
    if not len(result) > 0:
        raise InvalidUsage('no loads were found for the specified caliber, please try again')
    LOGGER.info(f'{result}')
    return jsonify(f'{result}')

