from flask import jsonify
from dao.forumpost_dao import ForumPost
from database.db import db


def get_roomies_repo(page, per_page, city_id=None):
    query = ForumPost.query

    if city_id:
        query = query.filter_by(city_id=city_id)

    total = query.count()
    pagination = query.order_by(ForumPost.date_posted.asc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    roomies = pagination.items
    return roomies, total


def save_roomie_repo(roomie):
    db.session.add(roomie)
    db.session.commit()
    return roomie.as_dict()


def get_roomies_by_user_id_repo(user_id):
    roomies = ForumPost.query.filter_by(user_id=user_id).all()
    return roomies


def get_roomie_by_id_repo(id):
    roomie = ForumPost.query.filter_by(id=id).first()
    return roomie


def delete_roomie_by_id_repo(roomie_id):
    roomie = ForumPost.query.get(roomie_id)
    if roomie:
        db.session.delete(roomie)
        db.session.commit()
        return True
    return False


def edit_roomie_repo(roomie, roomie_data):
    for key, value in roomie_data.items():
        setattr(roomie, key, value)
    db.session.commit()
    return jsonify({"message": "Roomie updated successfully"}), 200
