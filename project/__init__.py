from flask import Flask, jsonify
from flask_session import Session
from flask_pymongo import PyMongo

server_session = Session()
mongo = PyMongo()


def create_app(config_file = None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_pyfile(config_file)
    extensions(app)
    blueprints(app)
    handle_error(app)
    return app


def extensions(app):
    server_session.init_app(app)
    mongo.init_app(app)


def blueprints(app):
    from .user import user_bp
    app.register_blueprint(user_bp)


def handle_error(app):
    @app.errorhandler(Exception)
    def err_handler(e):
        return jsonify({'error': str(e), 'data': None})
