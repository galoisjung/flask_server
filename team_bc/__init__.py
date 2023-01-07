from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    # database 정보
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    from team_bc.views import api
    app.register_blueprint(api.bp)

    return app
