from flask_marshmallow import Marshmallow
from dao.message_dao import Message

ma = Marshmallow()


class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
        fields = ("id", "chat_id", "text", "user_id", "date_posted")
