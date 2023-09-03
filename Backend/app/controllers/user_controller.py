from flask import jsonify, request
from app.repositories.user_repository import (
    get_user_by_email_repo,
    get_user_by_id_repo,
    get_user_by_username_repo,
    get_users_repo,
    save_user_repo,
    update_user_repo,
)
from utils.password import random_password, pwd_generated
from dao.user_dao import User
from utils.email import send_confirmation_email, send_password_email
from werkzeug.security import generate_password_hash, check_password_hash
from utils.validations import (
    hash_password,
    str_to_bool,
    validate_email,
    validate_password,
)


def get_users_controller():
    data = get_users_repo()
    if not data:
        return "NOT_FOUND_MSG"
    else:
        users_dicts = []
        for user in data:
            users_dicts.append(user.as_dict())
        return users_dicts


def save_user_controller():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    name = request.form["name"]
    surname = request.form["surname"]
    role = "user"
    instagram = request.form["instagram"]
    description = request.form["description"]
    smoke = str_to_bool(request.form["smoke"])
    work = str_to_bool(request.form["work"])
    study = str_to_bool(request.form["study"])
    birth = request.form["birth"]
    image = request.files.get("image")
    if not validate_email(email):
        return "email no valido"
    if not validate_password(password):
        return "La contraseña debe tener al menos 8 caracteres,una mayuscula, una minuscula y un caracter no alfanumerico"

    is_username_repeated = get_user_by_username_repo(username)
    if is_username_repeated:
        return "Usuario repetido"
    is_email_repeated = get_user_by_email_repo(email)
    if is_email_repeated:
        return "Email repetido"

    hashed_password = hash_password(password)
    from utils.upload import upload_profile_image

    if image:
        file = upload_profile_image(username, image, None)
    else:
        file = None

    user_by_request = User(
        smoke=smoke,
        instagram=instagram,
        description=description,
        work=work,
        study=study,
        birth=birth,
        username=username,
        email=email,
        password=hashed_password,
        name=name,
        surname=surname,
        role=role,
        image=file,
    )
    user_saved = save_user_repo(user_by_request)
    send_confirmation_email(email)
    return user_saved.as_dict()


def get_user_by_id_controller(user_id):
    user = get_user_by_id_repo(user_id)
    return user


def update_user_controller(user_id, jwt_image):
    user = get_user_by_id_repo(user_id)
    user.email = request.form["email"]
    user.name = request.form["name"]
    user.surname = request.form["surname"]
    user.role = "user"
    user.instagram = request.form["instagram"]
    user.description = request.form["description"]
    user.smoke = str_to_bool(request.form["smoke"])
    user.work = str_to_bool(request.form["work"])
    user.tudy = str_to_bool(request.form["study"])
    user.birth = request.form["birth"]
    image_file = request.files.get("image")
    if not validate_email(user.email):
        return "email no valido"
    if image_file:
        from utils.upload import upload_profile_image

        image = upload_profile_image(user.username, image_file, jwt_image)
        user.image = image
    update_user_repo()
    return user


def update_password_email_controller():
    data = request.get_json()
    username = data["username"]
    user = get_user_by_username_repo(username)

    if not user:
        return "No se ha encontrado ningun usuario con ese nombre"

    if username in pwd_generated and pwd_generated[username]:
        return "Ya se ha enviado un correo con la contraseña"

    new_pass = random_password(username)

    email = user.email
    send_password_email(email, username, new_pass)
    user.password = generate_password_hash(new_pass)
    update_user_repo()

    pwd_generated[username] = True

    return jsonify(message="Email enviado")


def update_password_controller(user_id):
    data = request.get_json()
    if not data:
        return "Error al cambiar la contraseña"
    new_pass = data["password"]
    if new_pass is not None and validate_password(new_pass):
        user = get_user_by_id_repo(user_id)
        if check_password_hash(user.password, new_pass):
            return "Contraseña repetida"
        user.password = generate_password_hash(new_pass)
        username = user.username
        pwd_generated[username] = False
        update_user_repo()
        return jsonify(message="Contraseña Actualizada")
    return "Formato de contraseña invalido"
