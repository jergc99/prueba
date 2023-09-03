from flask import Blueprint, request
from flask_cors import cross_origin
from app.controllers.room_controller import get_rooms_controller
from app.controllers.roomcontent_controller import (
    get_room_content_by_room_id_controller,
)
from app.controllers.roomie_controller import get_roomies_controller

from app.controllers.user_controller import (
    get_user_by_id_controller,
    save_user_controller,
    update_password_email_controller,
)

public_routes = Blueprint("public_routes", __name__, url_prefix="/api/public")


def register_public_routes(app):
    app.register_blueprint(public_routes)


@cross_origin
@public_routes.post("/save")
def save_user_public_routes():
    return save_user_controller()


@public_routes.get("/rooms")
def get_rooms_public_routes():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    city_id = request.args.get("city_id", type=int)
    return get_rooms_controller(page, per_page, city_id)


@public_routes.get("/all-rooms")
def get_all_rooms_public_routes():
    return get_rooms_controller()


@public_routes.get("/roomies")
def get_roomies_public_routes():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    city_id = request.args.get("city_id", type=int)
    return get_roomies_controller(page, per_page, city_id)


@public_routes.get("/user/<int:user_id>")
def get_user_full_name_by_id_public_routes(user_id):
    user = get_user_by_id_controller(user_id)
    name = user.name + " " + user.surname
    return {"name": name}


@public_routes.put("/password")
def update_password_email_routes():
    return update_password_email_controller()


@public_routes.get("/get-room-content/<int:room_id>")
def get_room_content__by_room_id_public_routes(room_id):
    return get_room_content_by_room_id_controller(room_id)
