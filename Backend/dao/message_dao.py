from database.db import db


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey("chats.user_id_1"), nullable=True)
    text = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    date_posted = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )

    users = db.relationship("User", backref="users")
    chats = db.relationship("Chat", backref="chats")

    def __init__(self, chat_id, text, user_id, date_posted):
        self.chat_id = chat_id
        self.text = text
        self.user_id = user_id
        self.date_posted = date_posted

    def as_dict(self):
        return {
            "id": self.id,
            "chat_id": self.chat_id,
            "text": self.text,
            "user_id": self.user_id,
            "date_posted": self.date_posted.strftime("%Y-%m-%d %H:%M:%S"),
        }
