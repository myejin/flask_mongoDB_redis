from flask import Flask
from flask_session import Session
from flask_pymongo import PyMongo

# flask extension 전역범위에 생성 
server_session = Session()
mongo = PyMongo()

def create_app(config_file = None):
    app = Flask(__name__, instance_relative_config = True) #?
    app.config.from_pyfile(config_file)
    extensions(app)
    blueprints(app)
    return app

def extensions(app):
    server_session.init_app(app)
    mongo.init_app(app)

def blueprints(app):
    from .user import user_bp
    app.register_blueprint(user_bp)