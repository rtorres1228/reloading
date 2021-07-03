from flask import jsonify, Blueprint

loads_api = Blueprint('loads_api', __name__)


'''getter functions'''


@loads_api.route('/contributors')
def get_contributors():
    return jsonify('hello')


@loads_api.route('/loads')
def get_loads():
    return jsonify('loads')

