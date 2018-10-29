from flask import Flask
from flask_jwt_extended import JWTManager
from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['JWT_SECRET_KEY'] = 'sweet-secret'
    jwt = JWTManager(app)

    # register the v1_blueprint
    from app.api import v1_blueprint
    app.register_blueprint(v1_blueprint)
    return app
