import requests
from data.data import url

class Order:
    @staticmethod
    def create_order(payload = None):
        if not payload:
            raise Exception('Order not passed')
        return requests.post(url + '/api/v1/orders', data=payload)

    @staticmethod
    def get_orders_list():
        return requests.get(url + '/api/v1/orders')

    @staticmethod
    def get_order_by_track(track=None):
        return requests.get(url + '/api/v1/orders/track' + ('?t=' + str(track) if track else ''))

    @staticmethod
    def accept_order(order_id=None, courier_id=None):
        return requests.put(url + '/api/v1/orders/accept/' + (str(order_id) if order_id else '') + ('?courierId=' + str(courier_id) if courier_id else ''))