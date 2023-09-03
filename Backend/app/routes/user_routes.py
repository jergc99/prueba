from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.controllers.city_controller import get_cities_controller
from app.controllers.room_controller import (
    delete_room_by_id_controller,
    edit_room_controller,
    get_rooms_by_user_id_controller,
    save_room_controller,
)
from app.controllers.roomcontent_controller import (
    delete_room_content_by_id_controller,
    get_room_content_count_controller,
    upload_room_content_controller,
)
from app.controllers.roomie_controller import (
    delete_roomie_by_id_controller,
    edit_roomie_controller,
    get_roomies_by_user_id_controller,
    save_roomie_controller,
)

from app.controllers.user_controller import (
    get_user_by_id_controller,
    get_users_controller,
    save_user_controller,
    update_password_controller,
    update_user_controller,
)
from app.repositories.room_repository import get_room_by_id_repo
from app.repositories.user_repository import get_user_by_id_repo


user_routes = Blueprint("user_routes", __name__, url_prefix="/api/user")


def register_user_routes(app):
    app.register_blueprint(user_routes)


@user_routes.get("")
def get_users_routes():
    return get_users_controller()


@user_routes.get("/<int:user_id>")
def get_user_by_id_public_routes(user_id):
    return get_user_by_id_controller(user_id).as_dict()


@user_routes.get("/jwt")
@jwt_required()
def get_self_info():
    current_user = get_jwt_identity()
    return current_user["user"]


@user_routes.put("/edit-profile")
@jwt_required()
def update_self_info():
    current_user = get_jwt_identity()
    print(current_user)
    user_id = current_user["user"]["id"]
    jwt_image = current_user["user"]["image"]
    update_user_controller(user_id, jwt_image)
    return current_user["user"]


@user_routes.post("/add-roomie")
@jwt_required()
def save_roomie_user_routes():
    current_user = get_jwt_identity()
    user_id = current_user["user"]["id"]
    return save_roomie_controller(user_id)


@user_routes.get("/cities")
def get_cities_user_routes():
    return get_cities_controller()


@user_routes.post("/add-room")
@jwt_required()
def save_room_user_routes():
    current_user = get_jwt_identity()
    user_id = current_user["user"]["id"]
    return save_room_controller(user_id)


@user_routes.post("/add-room-content/<int:room_id>")
@jwt_required()
def upload_room_content_routes(room_id):
    room = get_room_by_id_repo(room_id)
    user = get_user_by_id_repo(room.user_id)
    total = get_room_content_count_controller(room_id)
    if(total >= 10):
        return "El maximo de imagenes por Room es de 10"
    return upload_room_content_controller(user.username, room_id)


@user_routes.get("/my-rooms")
@jwt_required()
def get_my_rooms_user_routes():
    current_user = get_jwt_identity()
    user_id = current_user["user"]["id"]
    return get_rooms_by_user_id_controller(user_id)


@user_routes.get("/my-roomies")
@jwt_required()
def get_my_roomies_user_routes():
    current_user = get_jwt_identity()
    user_id = current_user["user"]["id"]
    return get_roomies_by_user_id_controller(user_id)


@user_routes.delete("/delete-room/<int:room_id>")
@jwt_required()
def delete_room_by_id_user_routes(room_id):
    current_user = get_jwt_identity()
    user_id = current_user["user"]["id"]
    delete_room_by_id_controller(room_id, user_id)
    return current_user


@user_routes.delete("/delete-roomie/<int:roomie_id>")
@jwt_required()
def delete_roomie_by_id_user_routes(roomie_id):
    current_user = get_jwt_identity()
    user_id = current_user["user"]["id"]
    delete_roomie_by_id_controller(roomie_id, user_id)
    return current_user


@user_routes.put("/edit-room/<int:room_id>")
@jwt_required()
def edit_room_user_routes(room_id):
    current_user = get_jwt_identity()
    user_id = current_user["user"]["id"]
    room_data = request.json
    return edit_room_controller(room_id, user_id, room_data)


@user_routes.put("/edit-roomie/<int:roomie_id>")
@jwt_required()
def edit_roomie_user_routes(roomie_id):
    current_user = get_jwt_identity()
    user_id = current_user["user"]["id"]
    roomie_data = request.json
    return edit_roomie_controller(roomie_id, user_id, roomie_data)


@user_routes.put("/password")
@jwt_required()
def update_password_routes():
    current_user = get_jwt_identity()
    user_id = current_user["user"]["id"]
    return update_password_controller(user_id)


@user_routes.delete("/delete-room-content/<int:content_id>")
@jwt_required()
def delete_room_content_by_id_routes(content_id):
    current_user = get_jwt_identity()
    user_id = current_user["user"]["id"]  
    return delete_room_content_by_id_controller(content_id, user_id)
