import allure
import requests
import pytest

from data import Data, Endpoints
data = Data()
end = Endpoints()

from helpers import register_new_courier_and_return_login_password, generate_random_string

class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    @allure.description("Проверка, что курьер успешно создается")
    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(end.URL + end.CREATE_COURIER_END, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title("Ошибка повторного создания одного и того же курьера")
    @allure.description("Проверка, что нельзя создать одного и того же курьера дважды")
    def test_create_courier_two_same_error_login(self):
        login_pass_list = register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass_list[0],
            "password": login_pass_list[1],
            "first_name": login_pass_list[2]
        }
        response = requests.post(end.URL + end.CREATE_COURIER_END, data=payload)
        r = response.json()
        assert response.status_code == 409 and r["message"] == 'Этот логин уже используется. Попробуйте другой.'

    @pytest.mark.parametrize('payload', [
        {
            "login": data.EMPTY_FIELD,
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        },
        {
            "login": generate_random_string(10),
            "password": data.EMPTY_FIELD,
            "firstName": generate_random_string(10)
        }
    ])
    @allure.title("Ошибка создания курьера при отсутствии обязательных параметров")
    @allure.description("Проверка, что курьер не создастся, если какие-то обязательные параметры будут отсутствовать")
    def test_create_courier_empty_required_field_error_not_enough_data(self, payload):
        response = requests.post(end.URL + end.CREATE_COURIER_END, data=payload)
        r = response.json()
        assert response.status_code == 400 and r["message"] == 'Недостаточно данных для создания учетной записи'
