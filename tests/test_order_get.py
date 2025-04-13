import pytest
import allure
from instances.order import Order

@allure.suite("Получить заказ по его номеру")
@pytest.mark.usefixtures("register_and_delete")
class TestOrderGet(Order):
    @allure.title("успешный запрос возвращает объект с заказом")
    def test_order_get_success(self, order_track):
        response = self.get_order_by_track(order_track)
        assert response.json()["order"]

    @allure.title("запрос без номера заказа возвращает ошибку")
    def test_order_get_without_track(self):
        response = self.get_order_by_track()
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("запрос с несуществующим заказом возвращает ошибку")
    def test_order_get_error_track(self):
        response = self.get_order_by_track(1234567)
        assert response.status_code == 404 and response.json()["message"] ==  "Заказ не найден"



