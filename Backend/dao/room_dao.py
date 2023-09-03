from database.db import db


class Room(db.Model):
    __tablename__ = "rooms"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    smoke = db.Column(db.Boolean, nullable=False, default=False)
    pet = db.Column(db.Boolean, nullable=False, default=False)
    priv_bath = db.Column(db.Boolean, nullable=False, default=False)
    n_baths = db.Column(db.Integer, nullable=False)
    n_rooms = db.Column(db.Integer, nullable=False)
    garage = db.Column(db.Boolean, nullable=False, default=False)
    n_roomies = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey("cities.id"), nullable=False)

    users = db.relationship("User", backref="users")

    def __init__(
        self,
        description,
        user_id,
        smoke,
        pet,
        priv_bath,
        n_baths,
        n_rooms,
        garage,
        n_roomies,
        price,
        location,
        title,
        city_id,
    ):
        self.description = description
        self.user_id = user_id
        self.smoke = smoke
        self.pet = pet
        self.priv_bath = priv_bath
        self.n_baths = n_baths
        self.n_rooms = n_rooms
        self.garage = garage
        self.n_roomies = n_roomies
        self.price = price
        self.location = location
        self.title = title
        self.city_id = city_id

    def as_dict(self):
        user = "Sin usuario"
        city = "Sin Ciudad"
        return {
            "id": self.id,
            "description": self.description,
            "user_id": self.user_id,
            "date_created": self.date_created.strftime("%Y-%m-%d"),
            "smoke": self.smoke,
            "pet": self.pet,
            "priv_bath": self.priv_bath,
            "n_baths": self.n_baths,
            "n_rooms": self.n_rooms,
            "garage": self.garage,
            "n_roomies": self.n_roomies,
            "price": self.price,
            "location": self.location,
            "title": self.title,
            "user_name": user,
            "city_id": self.city_id,
            "city_name": city,
        }
