from flask import jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from dao.user_dao import User
from dao_schema.user_schema import UserSchema


users_schema = UserSchema(many=True)


def login_controller():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).first()
    if not user:
        return "El usuario no existe"
    if not user.username == username:
        return "El username no existe"
    if check_password_hash(user.password, password):
        return "Contraseña incorrecta"
    access_token = create_access_token(identity={"user": user.as_dict()})
    return jsonify(access_token=access_token, user=user.as_dict())
