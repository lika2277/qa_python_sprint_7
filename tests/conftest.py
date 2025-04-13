import pytest
from data.data import orders
from instances.courier import Courier
from instances.order import Order

@pytest.fixture(scope="class")
def register_and_delete(request):
    request.cls.courier = Courier.register_and_return_new_courier()

    yield

    delete_response = Courier.delete_courier(request.cls.courier.get("id"))
    if delete_response.status_code != 200:
        raise Exception("Can't delete")

@pytest.fixture(scope="function", params = orders)
def order(request):
    return request.param

@pytest.fixture(scope="function")
def courier_id():
    courier = Courier.register_and_return_new_courier()
    return courier.get("id")

@pytest.fixture(scope="function")
def order_track(order):
    response = Order.create_order(order)
    return response.json()['track']

@pytest.fixture(scope="function")
def order_id(order_track):
    response = Order.get_order_by_track(order_track)
    return response.json()["order"]["id"]
