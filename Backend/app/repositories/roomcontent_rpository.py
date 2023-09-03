from flask import jsonify
from dao.roomcontent_dao import RoomContent
from database.db import db


def save_content(room_id, content, title):
    new_content = RoomContent(room_id=room_id, content=content, title=title)
    db.session.add(new_content)
    db.session.commit()
    return new_content


def get_room_content_by_room_id_repo(room_id):
    room_content = RoomContent.query.filter_by(room_id=room_id).all()
    return room_content


def get_room_content_by_id_repo(id):
    room_content = RoomContent.query.filter_by(id=id).first()
    return room_content


def delete_room_content_by_id_repo(content_id):
    content = RoomContent.query.get(content_id)
    if content:
        db.session.delete(content)
        db.session.commit()
        return jsonify("Borrado"), 200
    return False

def get_room_content_count_repo(room_id):
    total = RoomContent.query.filter_by(room_id=room_id).count()
    return total
