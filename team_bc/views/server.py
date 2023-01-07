from flask import Flask, request, jsonify, request, Blueprint
from flask_cors import CORS

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/login', methods=['GET', 'POST'])
def userLogin():
    if request.method == "GET":
        user = request.get_json()  # json 데이터를 받아옴
        return jsonify(user)  # 받아온 데이터를 다시 전송
    elif request.method == "POST":
        user = request.get_json()  # json 데이터를 받아옴
    return jsonify(user)  # 받아온 데이터를c 다시 전송


@bp.route('/register', methods=['GET', 'POST'])
def userRegister():
    if request.method == "GET":
        user = request.get_json()  # json 데이터를 받아옴
        return jsonify(user)  # 받아온 데이터를 다시 전송
    elif request.method == "POST":
        user = request.get_json()  # json 데이터를 받아옴
    return jsonify(user)  # 받아온 데이터를c 다시 전송


@bp.route('/environments/<language>')
def environments(language):
    return jsonify({"language": language})