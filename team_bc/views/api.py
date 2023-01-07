from flask import request, jsonify, Blueprint

from team_bc.models.Infomation import Information

# from models import Phishing

# 명령어
# flask db init
# flask db migrate
# flask db upgrade


# create a table


# def save(self):
#     db.session.add(self)
#     db.session.commit()
#
# @staticmethod
# def get_all():
#     return Information.query.all()
#
# def repr(self):
#     return f"<Information('{self.id}', '{self.password}, '{self.email}', '{self.name}')>"
#
# # def ():
# #


##################################################################################################################
# server
# @app.route("/")
# def main():
#     return render_template('index.js')


# 1. register -> post, login -> post
bp = Blueprint('api', __name__, url_prefix='/api/phishing/')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.is_json:
            # --------------------------------- data 들어오는 것인지 or id, pw, email 하나하나 만들어 주어야 하는 것인지
            data = request.get_json()

            id = data['id']
            password = data['pw']
            email = data['email']
            name = data['name']
            # -------------------------------------------- (1) response (원래 만들었던 server.py 참고하여 작성...?) -> (2) UI 작성
            # ---------------------------------- DataBase 와 연결
            info = Information(id=id, password=password, email=email, name=name)
            from team_bc import db
            db.session.add(info)
            db.session.commit()

            response = jsonify({
                "test": "test"
            })
        else:
            response = jsonify({
                "test", "test"
            })
            response.status_code = 201
        return response


# ----------------------------------------- route -> post (login)
@bp.route('/database', methods=['GET', 'POST'])
def get_database():
    information_all = Information.get_all()
    results = []

    for info in information_all:
        obj = {
            'url': info.url
        }
        results.append(obj)
    response = jsonify(results)
    response.status_code = 200
    return response


# 데이터베이스 연결
@bp.route('/count', methods=['GET'])
def get_counts():
    information_all = Information.get_all()
    count = len(information_all)
    response = jsonify({
        'count': count
    })
    response.status_code = 200
    return response
