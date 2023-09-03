from database.db import db
from dao.user_dao import User


def get_users_repo():
    users = User.query.all()
    return users


def save_user_repo(user):
    db.session.add(user)
    db.session.commit()
    return user


def get_user_by_username_repo(username):
    user = User.query.filter_by(username=username).first()
    return user


def get_user_by_email_repo(email):
    user = User.query.filter_by(email=email).first()
    return user


def get_user_by_id_repo(id):
    user_by_id = User.query.filter_by(id=id).first()
    return user_by_id


def update_user_repo():
    db.session.commit()
