from flask_marshmallow import Marshmallow

from dao.user_dao import User

ma = Marshmallow()


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "name",
            "surname",
            "role",
            "image",
            "date_created",
            "smoke",
            "instagram",
            "description",
            "work",
            "study",
            "age",
        )
