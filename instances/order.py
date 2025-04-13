import requests
import allure
from data.data import endpoint_orders

class Order:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload = None):
        if not payload:
            raise Exception('Order not passed')
        return requests.post(endpoint_orders, data=payload)

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders_list():
        return requests.get(endpoint_orders)


    @staticmethod
    @allure.step("Получить заказ по треку")
    def get_order_by_track(track=None):
        return requests.get(endpoint_orders + "/track" + ('?t=' + str(track) if track else ''))

    @staticmethod
    @allure.step("Принять заказ")
    def accept_order(order_id=None, courier_id=None):
        return requests.put(endpoint_orders + "/accept/" + (str(order_id) if order_id else '') + ('?courierId=' + str(courier_id) if courier_id else ''))