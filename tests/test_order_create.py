import json
import allure
from instances.order import Order

@allure.suite("Создание заказа")
class TestOrderCreate(Order):
    @allure.title("можно указать один из цветов — BLACK или GREY")
    def test_create_order_with_color(self, order):
        order["color"] = ["BLACK"]
        response = self.create_order(json.dumps(order))
        assert response.status_code == 201

    @allure.title("можно указать оба цвета")
    def test_create_order_with_all_colors(self, order):
        order["color"] = ["BLACK", "GREY"]
        response = self.create_order(json.dumps(order))
        assert response.status_code == 201

    @allure.title("можно совсем не указывать цвет")
    def test_create_order_without_color(self, order):
        order["color"] = []
        response = self.create_order(json.dumps(order))
        assert response.status_code == 201

    @allure.title("тело ответа содержит track")
    def test_create_order_has_track(self, order):
        response = self.create_order(json.dumps(order))
        assert response.status_code == 201 and response.json()["track"]


