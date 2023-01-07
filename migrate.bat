set FLASK_APP=team_bc/__init__.py
set FLASK_ENV=development
flask db init
flask db migrate
flask db upgrade
