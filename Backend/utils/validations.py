from datetime import datetime
import re
from flask_jwt_extended import get_jwt_identity
from werkzeug.security import generate_password_hash

from app.repositories.user_repository import get_user_by_id_repo


def hash_password(password):
    hashed_password = generate_password_hash(password)
    return hashed_password


def validate_email(email):
    email_regex = r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"
    if re.match(email_regex, email):
        return True
    return False


def validate_password(password):
    if len(password) < 8:
        return False
    if not any(letter.isupper() for letter in password):
        return False
    if not re.search("[!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]", password):
        return False
    if not any(letter.isdigit() for letter in password):
        return False
    return True


def calculate_age(birth_date: datetime):
    today = datetime.today()
    age = (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )
    return age


def str_to_bool(value):
    """Convierte un string 'true' o 'false' a su respectivo valor booleano."""
    value = value.lower().strip()
    if value == "true":
        return True
    elif value == "false":
        return False
    else:
        raise ValueError(f"Valor inválido para campo booleano: {value}")
    
def isAdmin(user_id):
    user = get_user_by_id_repo(user_id)
    if user.role == 'admin':
        return True
    else:
        return False
