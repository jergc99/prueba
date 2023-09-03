from app.repositories.city_repository import get_cities_repo


def get_cities_controller():
    return get_cities_repo()