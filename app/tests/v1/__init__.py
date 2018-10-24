from flask import Flask
# import configurations dictionary
from Instance.config import app_config


# create the application's instance
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    with app.app_context():
        from api.v1.models.users import User
    # add a configuration setting
    app.config.from_object(app_config[config_name])
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'

    # register the v1_blueprint
    from app.api import v1_blueprint
    app.register_blueprint(v1_blueprint)
    return app
