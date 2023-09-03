from database.db import db


class RoomContent(db.Model):
    __tablename__ = "room_content"

    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    title = db.Column(
        db.String(100), nullable=True
    )

    room = db.relationship("Room", backref="room_contents")

    def __init__(self, room_id, content, title=None):
        self.room_id = room_id
        self.content = content
        self.title = title

    def as_dict(self):
        return {
            "id": self.id,
            "room_id": self.room_id,
            "content": self.content,
            "title": self.title,
        }
