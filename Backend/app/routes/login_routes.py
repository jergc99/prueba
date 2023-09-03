from flask import Blueprint
from flasgger import swag_from

from app.controllers.login_controller import login_controller

login_routes = Blueprint("login_routes", __name__, url_prefix="/api")


def register_login_routes(app):
    app.register_blueprint(login_routes)


@login_routes.post("/login")
def login_route():
    return login_controller()
