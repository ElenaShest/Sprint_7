# Sprint_7
# Проект автоматизации тестирования API сайта заказа самокатов

1. Основа для написания автотестов — фреймворк pytest.
2. Команда для запуска — pytest -v .\test

Тесты:
1. test_create_courier - файл с тестами регистрации курьера
   2. test_create_courier_success - успешная регистрация
   3. test_create_courier_two_same_error_login - двойное создание одного и того же курьера
   4. test_create_courier_empty_required_field_error_not_enough_data - создание курьера при отсутствующих обязательных параметрах
5. test_login_courier - файл с тестами авторизации курьера
   6. test_login_courier_all_fields_success - успешная авторизация
   7. test_login_courier_wrong_field_error_not_found - авторизация при некорректных параметрах
   8. test_login_courier_empty_field_error_not_enough_data - авторизация при отсутствующих параметрах
9. test_create_order - файл с тестами создания заказа
   10. test_create_order - создание заказа с разными параметрами
11. test_order_list - файл с тестами запроса списка заказов
    12. test_order_list - получение списка заказов
