from flask import jsonify
from dao.room_dao import Room
from database.db import db


def get_rooms_repo(page, per_page, city_id=None):
    query = Room.query
    if city_id:
        query = query.filter_by(city_id=city_id)
    total = query.count()
    pagination = query.order_by(Room.date_created.asc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    rooms = pagination.items
    return rooms, total


def save_room_repo(room):
    db.session.add(room)
    db.session.commit()
    return room.as_dict()


def get_rooms_by_user_id_repo(user_id):
    rooms = Room.query.filter_by(user_id=user_id).all()
    return rooms


def get_room_by_id_repo(id):
    room = Room.query.filter_by(id=id).first()
    return room


def delete_room_by_id_repo(room_id):
    room = Room.query.get(room_id)
    if room:
        db.session.delete(room)
        db.session.commit()
        return True
    return False


def edit_room_repo(room, room_data):
    for key, value in room_data.items():
        setattr(room, key, value)
    db.session.commit()
    return jsonify({"message": "Room updated successfully"}), 200
