from flask import jsonify, request
from app.repositories.room_repository import get_room_by_id_repo

from app.repositories.roomcontent_rpository import (
    delete_room_content_by_id_repo,
    get_room_content_by_id_repo,
    get_room_content_by_room_id_repo,
    get_room_content_count_repo,
    save_content,
)
from utils.validations import isAdmin


def upload_room_content_controller(username, room_id):
    try:
        room_id = str(room_id)
        title = "Titulo"
        file = request.files.get("file")
        from utils.upload import save_image
        file_url = save_image(file, username, room_id)
        room_content = save_content(room_id, file_url, title)
        return jsonify(room_content.as_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def get_room_content_by_room_id_controller(room_id):
    room_content = get_room_content_by_room_id_repo(room_id)
    if not room_content:
        return "No se encontraron imagenes"
    else:
        room_content_dict = []
        for content in room_content:
            content_dict = content.as_dict()
            room_content_dict.append(content_dict)
        return room_content_dict


def delete_room_content_by_id_controller(content_id, user_id):
    content = get_room_content_by_id_repo(content_id)
    room = get_room_by_id_repo(content.room_id)
    if (user_id == room.user_id) or isAdmin(user_id):
        from utils.upload import delete_image
        delete_image(content.content)
        return delete_room_content_by_id_repo(content_id)
    else:
        return "No se pudo borrar la imagen"
    
def get_room_content_count_controller(room_id):
    return get_room_content_count_repo(room_id)
