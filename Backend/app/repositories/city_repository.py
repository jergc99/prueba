from dao.city_dao import City


def get_city_by_id_repo(id):
    city = City.query.filter_by(id=id).first()
    return city


def get_cities_repo():
    cities = City.query.order_by(City.name.asc()).all()
    return [city.as_dict() for city in cities]
