from flask import Flask
from api import loads_api


app = Flask(__name__)

app.register_blueprint(loads_api)


if __name__ == "__main__":
    app.run(debug=True)
