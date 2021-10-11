import atexit
import logging
import time
from flask import jsonify, Blueprint, Flask, request
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


@loads_api.route('/bootstrap/db')
def boot_strap():
    LOGGER.info('dropping all schema')
    Base.metadata.drop_all(engine)
    LOGGER.info('finished dropping all schema')
    time.sleep(3)
    LOGGER.info('bootstraping the schema')
    Base.metadata.create_all(engine)
    LOGGER.info('finished bootstrapping the schema')
    return jsonify({'result': 'finished bootstrapping the schema'})


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
        raise InvalidUsage('no loads were found in the db', status_code=404)
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
        raise InvalidUsage('no loads were found please try again', status_code=404)
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
        raise InvalidUsage('no loads were found please try again', status_code=404)
    return jsonify(f'{result}')

@loads_api.route('/caliber/<caliber>/all')
def get_load__caliber(caliber):
    caliber = '%{}%'.format(caliber)
    session = Session()
    loads_for_caliber = session.query(Caliber, Load, Contributor).join(Caliber, Contributor.calibers).filter(Caliber.caliber_name.like(caliber)).join(Load, Caliber.loads).all()
    result = result_dict(loads_for_caliber)
    session.commit()
    if not len(result) > 0:
        raise InvalidUsage('no loads were found for the specified caliber, please try again', status_code=404)
    LOGGER.info(f'{result}')
    return jsonify(f'{result}')


@loads_api.route('/enter_one_load/<user_name>/<email>', methods=['POST'])
def insert_one_record(user_name, email):
    if request.method == 'POST':
        user_name = user_name
        email = email
        session = Session()
        contributor = Contributor(user_name, email)
        caliber = Caliber('45 acp')
        load = Load('strong load', 230, 'Tite Group', 4.3, 'CCI', 'P', 'S')
        contributor.calibers = [caliber]
        caliber.loads = [load]
        session.add(contributor)
        session.add(caliber)
        session.add(load)
        session.commit()
    else:
        raise InvalidUsage('this end point only accepts Post Method', status_code=400)
