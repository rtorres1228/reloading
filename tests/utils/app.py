import pytest

from flask import Flask
from api import loads_api


app = Flask(__name__)

app.register_blueprint(loads_api)

@pytest.fixture(scope='module')
def getapp():
    return app.run(debug=True)