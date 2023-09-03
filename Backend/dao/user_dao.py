from database.db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=False, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=db.func.current_timestamp()
    )
    role = db.Column(db.Enum("admin", "user"), nullable=False, default="user")
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    smoke = db.Column(db.Boolean, nullable=False, default=False)
    instagram = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    work = db.Column(db.Boolean, nullable=False, default=False)
    study = db.Column(db.Boolean, nullable=False, default=True)
    birth = db.Column(db.Date, nullable=False)
    approved = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(
        self,
        username,
        email,
        password,
        name,
        surname,
        description,
        smoke,
        instagram,
        role,
        work,
        study,
        birth,
        approved=False,
        image=None,
    ):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.description = description
        self.image = image
        self.smoke = smoke
        self.instagram = instagram
        self.study = study
        self.role = role
        self.work = work
        self.birth = birth
        self.approved = approved

    def as_dict(self):
        from utils.validations import calculate_age

        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "surname": self.surname,
            "role": self.role,
            "image": self.image,
            "date_created": self.date_created.strftime("%Y-%m-%d"),
            "smoke": self.smoke,
            "instagram": self.instagram,
            "description": self.description,
            "work": self.work,
            "study": self.study,
            "birth": self.birth,
            "age": calculate_age(self.birth),
            "approved": self.approved,
        }
