from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    # database 정보



    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0399@localhost:5432/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    from team_bc.views import server
    app.register_blueprint(server.bp)
    from team_bc.views import api
    app.register_blueprint(api.bp)

    return app