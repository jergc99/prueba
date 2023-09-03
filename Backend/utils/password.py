import random
import string

pwd_generated = {}


def random_password(username):
    if username in pwd_generated and pwd_generated[username]:
        return "Ya se generó una contraseña. Por favor, cambie su contraseña antes de utilizar esta funcionalidad nuevamente."
    min_length = 8
    caracteres = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = (
            random.choices(string.ascii_uppercase)
            + random.choices(string.ascii_lowercase)
            + random.choices(string.digits)
            + random.choices(string.punctuation)
            + random.choices(caracteres, k=min_length - 4)
        )
        random.shuffle(password)
        password = "".join(password)

        if (
            any(c.isupper() for c in password)
            and any(c.islower() for c in password)
            and any(c.isdigit() for c in password)
            and any(not c.isalnum() for c in password)
        ):
            return password
