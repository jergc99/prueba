from flask_marshmallow import Marshmallow
from dao.chat_dao import Chat

ma = Marshmallow()


class ChatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Chat
        fields = ("user_id_1", "user_id_2")
