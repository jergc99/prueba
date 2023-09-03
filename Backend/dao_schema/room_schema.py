from flask_marshmallow import Marshmallow
from dao.room_dao import Room

ma = Marshmallow()


class RoomSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Room
        fields = (
            "id",
            "description",
            "user_id",
            "date_created",
            "smoke",
            "pet",
            "priv_bath",
            "n_baths",
            "n_rooms",
            "garage",
            "n_roomies",
            "price",
            "location",
            "title",
        )
