from flask import request
from app.controllers.user_controller import get_user_by_id_controller
from app.repositories.city_repository import get_city_by_id_repo
from app.repositories.room_repository import (
    delete_room_by_id_repo,
    edit_room_repo,
    get_room_by_id_repo,
    get_rooms_by_user_id_repo,
    get_rooms_repo,
    save_room_repo,
)
from dao.room_dao import Room
from dao_schema.room_schema import RoomSchema
from utils.validations import isAdmin


room_schema = RoomSchema(many=True)


def get_rooms_controller(page, per_page, city_id):
    data, total = get_rooms_repo(page, per_page, city_id)
    if not data:
        return "No se encontraron habitaciones"
    else:
        rooms_dicts = []
        for room in data:
            room_dict = room.as_dict()
            user_id = room_dict.get("user_id")
            user = get_user_by_id_controller(user_id)
            room_dict["user_name"] = user.name + " " + user.surname
            city = get_city_by_id_repo(room.city_id)
            room_dict["city_name"] = city.name
            rooms_dicts.append(room_dict)
        return {"total": total, "rooms": rooms_dicts}


def get_all_rooms_controller():
    return


def save_room_controller(user_id):
    description = request.json["description"]
    smoke = request.json["smoke"]
    pet = request.json["pet"]
    priv_bath = request.json["priv_bath"]
    n_baths = request.json["n_baths"]
    n_rooms = request.json["n_rooms"]
    garage = request.json["garage"]
    n_roomies = request.json["n_roomies"]
    price = request.json["price"]
    location = request.json["location"]
    title = request.json["title"]
    city = request.json[
        "city_id"
    ]

    room = Room(
        description=description,
        user_id=user_id,
        smoke=smoke,
        pet=pet,
        priv_bath=priv_bath,
        n_baths=n_baths,
        n_rooms=n_rooms,
        garage=garage,
        n_roomies=n_roomies,
        price=price,
        location=location,
        title=title,
        city_id=city,
    )

    return save_room_repo(room)


def get_rooms_by_user_id_controller(user_id):
    rooms = get_rooms_by_user_id_repo(user_id)
    if not rooms:
        return "No se encontraron habitaciones"
    else:
        rooms_dicts = []
        for room in rooms:
            room_dict = room.as_dict()
            user_id = room_dict.get("user_id")
            user = get_user_by_id_controller(user_id)
            room_dict["user_name"] = user.name + " " + user.surname
            city = get_city_by_id_repo(room.city_id)
            room_dict["city_name"] = city.name
            rooms_dicts.append(room_dict)
        return rooms_dicts


def delete_room_by_id_controller(room_id, user_id):
    room = get_room_by_id_repo(room_id)
    if (room.user_id == user_id) or isAdmin(user_id):
        return delete_room_by_id_repo(room_id)
    else:
        return "No puedes borrar esta habitacion"


def edit_room_controller(room_id, user_id, room_data):
    room = get_room_by_id_repo(room_id)
    if room and room.user_id == user_id or isAdmin(user_id):
        return edit_room_repo(room, room_data)
    else:
        return "No puedes editar esta habitacion"
