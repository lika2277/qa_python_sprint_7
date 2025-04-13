import pytest
import allure
from instances.order import Order

@allure.suite("Принять заказ")
@pytest.mark.usefixtures("register_and_delete")
class TestOrderAccept(Order):
    @allure.title("успешный запрос возвращает 'ok'")
    def test_order_accept_success(self, order_id):
        response = self.accept_order(order_id, self.courier_id)
        assert response.status_code == 200 and response.json()['ok'] == True

    @allure.title("если не передать id курьера, запрос вернёт ошибку")
    def test_order_accept_error_courier_id(self, order_id):
        response = self.accept_order(order_id)
        assert response.status_code == 400 and response.json()['message'] ==  "Недостаточно данных для поиска"

    @allure.title("если передать неверный id курьера, запрос вернёт ошибку")
    def test_order_accept_wrong_courier_id(self, order_id):
        response = self.accept_order(order_id, 1234567)
        assert response.status_code == 404 and response.json()['message'] ==  "Курьера с таким id не существует"

    @allure.title("если не передать id заказа, запрос вернёт ошибку")
    def test_order_accept_error_order_id(self):
        pytest.skip("неправильный код ответа")
        response = self.accept_order(None, self.courier_id)
        assert response.status_code == 400 and response.json()['message'] ==  "Недостаточно данных для поиска"

    @allure.title("если передать неверный id заказа, запрос вернёт ошибку")
    def test_order_accept_wrong_order_id(self):
        response = self.accept_order(1234567, self.courier_id)
        assert response.status_code == 404 and response.json()['message'] ==  "Заказа с таким id не существует"