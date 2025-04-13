import random
import string
import allure
import requests
from data.data import endpoint_courier

class Courier:
    @staticmethod
    @allure.step("Генерация нового курьера")
    def generate_new_courier():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        return {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "first_name": generate_random_string(10)
        }

    @staticmethod
    @allure.step("Регистрация курьера")
    def register_new_courier(payload = None):
        if not payload:
            raise Exception('Courier not passed')
        return requests.post(endpoint_courier, data=payload)

    @staticmethod
    @allure.step("Авторизация курьера")
    def login_courier(payload = None):
        if not payload:
            raise Exception('Courier login and password not passed')
        return requests.post(endpoint_courier + '/login', data=payload)

    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(payload = None):
        return requests.delete(endpoint_courier + "/" + (str(payload) if payload else ''))

    @staticmethod
    @allure.step("Регистрация нового курьера и возвращние его описания")
    def register_and_return_new_courier():
        courier = Courier.generate_new_courier()

        register_response = Courier.register_new_courier(courier)
        if register_response.status_code != 201:
            raise Exception("Can't register new courier")

        login_response = Courier.login_courier(courier)
        if login_response.status_code != 200:
            raise Exception("Can't login")

        courier["id"] = login_response.json()["id"]
        return courier