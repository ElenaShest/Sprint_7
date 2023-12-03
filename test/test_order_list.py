import allure
import requests

from data import Endpoints
end = Endpoints()

class TestOrderList:

    @allure.title("Получение списка заказов")
    @allure.description("Проверка, что список заказов приходит в правильном формате")
    def test_order_list(self):
        response = requests.get(end.URL + end.ORDER_END)
        r = response.json()
        assert response.status_code == 200 and type(r["orders"]) == list
