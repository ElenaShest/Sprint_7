import json

import allure
import requests
import pytest

from data import Data, Endpoints
data = Data()
end = Endpoints()

from helpers import generate_random_string

class TestCreateOrder:

    @pytest.mark.parametrize('firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color', [
        (generate_random_string(10), generate_random_string(10), data.RANDOM_ADDRESS, data.RANDOM_METRO_STATION, data.RANDOM_PHONE, data.RANDOM_RENT_TIME, data.RANDOM_DELIVERY_DATE, generate_random_string(10), [data.EMPTY_FIELD]),
        (generate_random_string(10), generate_random_string(10), data.RANDOM_ADDRESS, data.RANDOM_METRO_STATION, data.RANDOM_PHONE, data.RANDOM_RENT_TIME, data.RANDOM_DELIVERY_DATE, generate_random_string(10), ["BLACK"]),
        (generate_random_string(10), generate_random_string(10), data.RANDOM_ADDRESS, data.RANDOM_METRO_STATION, data.RANDOM_PHONE, data.RANDOM_RENT_TIME, data.RANDOM_DELIVERY_DATE, generate_random_string(10), ["GREY"]),
        (generate_random_string(10), generate_random_string(10), data.RANDOM_ADDRESS, data.RANDOM_METRO_STATION, data.RANDOM_PHONE, data.RANDOM_RENT_TIME, data.RANDOM_DELIVERY_DATE, generate_random_string(10), ["BLACK", "GREY"])
    ])
    @allure.title("Успешное создание заказа при выборе разных цветов")
    @allure.description("Проверка, что заказ успешно создается при выборе разных цветов")
    def test_create_order(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color
                }
        payload_string = json.dumps(payload)
        response = requests.post(end.URL + end.CREATE_ORDER_END, data=payload_string)
        assert response.status_code == 201 and "track" in response.text

