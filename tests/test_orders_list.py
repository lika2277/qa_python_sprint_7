from instances.order import Order
import allure

@allure.title("Список заказов")
class TestOrdersList(Order):
    @allure.step("Проверь, что в тело ответа возвращается список заказов")
    def test_orders_list(self):
        response = self.get_orders_list()
        assert response.json()["orders"]