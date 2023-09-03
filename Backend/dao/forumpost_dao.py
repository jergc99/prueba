from database.db import db


class ForumPost(db.Model):
    __tablename__ = "forum_posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    city_id = db.Column(db.Integer, db.ForeignKey("cities.id"), nullable=False)

    def __init__(self, user_id, title, content, city):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.city_id = city

    def as_dict(self):
        city = "Sin ciudad"
        name = " "
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_name": name,
            "title": self.title,
            "content": self.content,
            "date_posted": self.date_posted.strftime("%Y-%m-%d"),
            "city_id": self.city_id,
            "city_name": city,
        }
