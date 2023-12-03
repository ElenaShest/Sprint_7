import random

from faker import Faker
fake = Faker(locale="ru_RU")

class Data:
    RIGHT_LOGIN = "elenashest"
    RIGHT_PASS = "1234"
    WRONG_LOGIN = "elenashest1"
    WRONG_PASS = "12345"
    EMPTY_FIELD = ""
    RANDOM_ADDRESS = fake.address()
    RANDOM_METRO_STATION = random.randint(1, 112)
    RANDOM_PHONE = f'+7{random.randint(9000000000, 9999999999)}'
    RANDOM_RENT_TIME = random.randint(1, 7)
    RANDOM_DELIVERY_DATE = f'2023-12-{random.randint(15, 31)}'


class Endpoints:
    URL = "https://qa-scooter.praktikum-services.ru"
    LOGIN_END = "/api/v1/courier/login"
    CREATE_COURIER_END = "/api/v1/courier"
    CREATE_ORDER_END = "/api/v1/orders"
    ORDER_END = "/api/v1/orders"
