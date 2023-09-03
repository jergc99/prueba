from flask import request
from app.controllers.user_controller import get_user_by_id_controller
from app.repositories.city_repository import get_city_by_id_repo
from app.repositories.roomies_repository import (
    delete_roomie_by_id_repo,
    edit_roomie_repo,
    get_roomie_by_id_repo,
    get_roomies_by_user_id_repo,
    get_roomies_repo,
    save_roomie_repo,
)
from dao.forumpost_dao import ForumPost
from utils.validations import isAdmin


def get_roomies_controller(page, per_page, city_id):
    data, total = get_roomies_repo(page, per_page, city_id)
    if not data:
        return "No se encontraron publicaciones"
    else:
        roomies_dicts = []
        for roomie in data:
            roomie_dict = roomie.as_dict()
            city = get_city_by_id_repo(roomie.city_id)
            roomie_dict["city_name"] = city.name
            user = get_user_by_id_controller(roomie.user_id)
            roomie_dict["user_name"] = user.name + " " + user.surname
            roomies_dicts.append(roomie_dict)
        return {"total": total, "rooms": roomies_dicts}


def save_roomie_controller(user_id):
    title = request.json["title"]
    print(title)
    content = request.json["content"]
    city = request.json["city"]

    roomie = ForumPost(user_id=user_id, title=title, content=content, city=city)

    return save_roomie_repo(roomie)


def get_roomies_by_user_id_controller(user_id):
    roomies = get_roomies_by_user_id_repo(user_id)
    if not roomies:
        return "No se encontraron publicaciones"
    else:
        roomies_dicts = []
        for roomie in roomies:
            roomie_dict = roomie.as_dict()
            city = get_city_by_id_repo(roomie.city_id)
            roomie_dict["city_name"] = city.name
            user = get_user_by_id_controller(roomie.user_id)
            roomie_dict["user_name"] = user.name + " " + user.surname
            roomies_dicts.append(roomie_dict)
        return roomies_dicts


def delete_roomie_by_id_controller(roomie_id, user_id):
    roomie = get_roomie_by_id_repo(roomie_id)
    if (roomie.user_id == user_id) or isAdmin(user_id):
        return delete_roomie_by_id_repo(roomie_id)
    else:
        return "No puedes borrar esta publicacion"


def edit_roomie_controller(roomie_id, user_id, roomie_data):
    roomie = get_roomie_by_id_repo(roomie_id)
    if (roomie.user_id == user_id) or isAdmin(user_id):
        return edit_roomie_repo(roomie, roomie_data)
    else:
        return "No puedes editar esta publicacion"
