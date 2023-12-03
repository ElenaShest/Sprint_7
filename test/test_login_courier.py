import allure
import requests
import pytest

from data import Data, Endpoints
data = Data()
end = Endpoints()

from helpers import register_new_courier_and_return_login_password

class TestLoginCourier:

    @allure.title("Успешная авторизация")
    @allure.description("Проверка, что авторизация курьера проходит успешно")
    def test_login_courier_all_fields_success(self):
        login_pass_list = register_new_courier_and_return_login_password()
        login = login_pass_list[0]
        password = login_pass_list[1]
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(end.URL + end.LOGIN_END, data=payload)
        assert response.status_code == 200 and "id" in response.text

    @pytest.mark.parametrize('payload', [
        {
            "login": data.WRONG_LOGIN,
            "password": data.RIGHT_PASS
        },
        {
            "login": data.RIGHT_LOGIN,
            "password": data.WRONG_PASS
        }
    ])
    @allure.title("Ошибка авторизации при неверных параметрах")
    @allure.description("Проверка, что авторизация не осуществляется из-за некорректных данных")
    def test_login_courier_wrong_field_error_not_found(self, payload):
        response = requests.post(end.URL + end.LOGIN_END, data=payload)
        r = response.json()
        assert response.status_code == 404 and r["message"] == 'Учетная запись не найдена'

    @pytest.mark.parametrize('payload', [
        {
            "login": data.EMPTY_FIELD,
            "password": data.RIGHT_PASS
        },
        {
            "login": data.RIGHT_LOGIN,
            "password": data.EMPTY_FIELD
        }
    ])
    @allure.title("Ошибка авторизации при отсутствии")
    @allure.description("Проверка, что авторизация не осуществляется из-за отсутствующих данных")
    def test_login_courier_empty_field_error_not_enough_data(self, payload):
        response = requests.post(end.URL + end.LOGIN_END, data=payload)
        r = response.json()
        assert response.status_code == 400 and r["message"] == 'Недостаточно данных для входа'
