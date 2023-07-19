from flask import Flask
from application.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    bcrypt.init_app(app)
    db.init_app(app)

    from application.public.route import public
    app.register_blueprint(public)

    from application.admin.route import admin
    app.register_blueprint(admin)

    from application.auth.route import auth
    app.register_blueprint(auth)
    migrate = Migrate(app, db)

    return app
