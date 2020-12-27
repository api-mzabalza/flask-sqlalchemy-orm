from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.config import Config

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import sqlalchemy

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False
    db.init_app(app)
    bcrypt.init_app(app)


    # Routes
    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.user import users

    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(users, url_prefix='/users')


    return app