import datetime
import secrets
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from app.routes.login_routes import register_login_routes
from app.routes.public_routes import register_public_routes
from app.routes.user_routes import register_user_routes
from flask_uploads import UploadSet, configure_uploads, IMAGES
from envs.dev.dev_env import config, get_database_config, get_mail_config
from database.db import init_app


app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = secrets.token_urlsafe(16)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=24)
jwt = JWTManager(app)

ma = Marshmallow(app)

app.config["JSON_AS_ASCII"] = False
CORS(app)

user = get_database_config().get("MYSQL_USER")
host = get_database_config().get("MYSQL_HOST")
password = get_database_config().get("MYSQL_PASSWORD")
database = get_database_config().get("DATABASE_NAME")
sql_track_modifications = get_database_config().get("SQLALCHEMY_TRACK_MODIFICATIONS")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://" + user + ":" + password + "@" + host + "/" + database
)

app.config["MAIL_SERVER"] = get_mail_config().get("MAIL_SERVER")
app.config["MAIL_PORT"] = get_mail_config().get("MAIL_PORT")
app.config["MAIL_USERNAME"] = get_mail_config().get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = get_mail_config().get("MAIL_PASSWORD")
app.config["MAIL_USE_TLS"] = get_mail_config().get("MAIL_USE_TLS")

mail = Mail(app)

photos = UploadSet("photos", IMAGES)

app.config["UPLOADED_PHOTOS_DEST"] = "static/images"
configure_uploads(app, photos)


init_app(app)

register_user_routes(app)
register_login_routes(app)
register_public_routes(app)

if __name__ == "__main__":
    app.config.from_object(config["dev"])
    app.run()
