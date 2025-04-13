from instances.order import Order
import allure

@allure.suite("Список заказов")
class TestOrdersList(Order):
    @allure.title("Проверь, что в тело ответа возвращается список заказов")
    def test_orders_list(self):
        response = self.get_orders_list()
        assert response.status_code == 200 and response.json()["orders"]