from flask import Flask, session
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_serialize import FlaskSerialize
from flask_sqlalchemy import SQLAlchemy
import config
from flask_session import Session

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
def create_app():
    app = Flask(__name__)
    # database 정보
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    from team_bc.views import api
    from team_bc.views import question_view
    app.register_blueprint(api.bp)
    app.register_blueprint(question_view.bp)
    Session(app)
    return app
