from database.db import db


class Chat(db.Model):
    __tablename__ = "chats"

    user_id_1 = db.Column(
        db.Integer, db.ForeignKey("users.id"), primary_key=True, nullable=False
    )
    user_id_2 = db.Column(
        db.Integer, db.ForeignKey("users.id"), primary_key=True, nullable=False
    )

    users = db.relationship("User", backref="users")

    def __init__(self, user_id_1, user_id_2):
        self.user_id_1 = user_id_1
        self.user_id_2 = user_id_2

    def as_dict(self):
        return {
            "user_id_1": self.user_id_1,
            "user_id_2": self.user_id_2,
        }
