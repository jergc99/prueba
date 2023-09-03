from flask_marshmallow import Marshmallow

from dao.forumpost_dao import ForumPost

ma = Marshmallow()


class ForumPostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ForumPost
        fields = ("id", "user_id", "title", "content", "date_posted")
