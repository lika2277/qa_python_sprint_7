import pytest
from data.data import orders
from instances.courier import Courier
from instances.order import Order

@pytest.fixture(scope="class")
def register_and_delete(request):
    courier = Courier.generate_new_courier()

    register_response = Courier.register_new_courier(courier)
    if register_response.status_code == 201:
        request.cls.courier = courier
    else:
        raise Exception("Can't register new courier")

    login_response = Courier.login_courier(courier)
    if login_response.status_code == 200:
        request.cls.courier_id = login_response.json()["id"]
    else:
        raise Exception("Can't login")

    yield

    delete_response = Courier.delete_courier(request.cls.courier_id)
    if delete_response.status_code != 200:
        raise Exception("Can't delete")

@pytest.fixture(scope="function", params = orders)
def order(request):
    return request.param

@pytest.fixture(scope="function")
def courier_id():
    courier = Courier.generate_new_courier()

    register_response = Courier.register_new_courier(courier)
    if register_response.status_code != 201:
        raise Exception("Can't register new courier")

    login_response = Courier.login_courier(courier)
    if login_response.status_code != 200:
        raise Exception("Can't login")

    return login_response.json()["id"]

@pytest.fixture(scope="function")
def order_track(order):
    response = Order.create_order(order)
    return response.json()['track']

@pytest.fixture(scope="function")
def order_id(order_track):
    response = Order.get_order_by_track(order_track)
    return response.json()["order"]["id"]
