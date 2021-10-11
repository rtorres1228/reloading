from flask import Flask
from api import loads_api, app


app.register_blueprint(loads_api)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
