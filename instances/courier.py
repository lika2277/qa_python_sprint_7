import random
import string

import allure
import requests
from data.data import url

class Courier:

    @allure.step("Генерация нового курьера")
    @staticmethod
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

    @allure.step("Регистрация курьера")
    @staticmethod
    def register_new_courier(payload = None):
        if not payload:
            raise Exception('Courier not passed')
        return requests.post(url + '/api/v1/courier', data=payload)

    @allure.step("Авторизация курьера")
    @staticmethod
    def login_courier(payload = None):
        if not payload:
            raise Exception('Courier login and password not passed')
        return requests.post(url + '/api/v1/courier/login', data=payload)

    @allure.step("Удаление курьера")
    @staticmethod
    def delete_courier(payload = None):
        return requests.delete(url + '/api/v1/courier/' + (str(payload) if payload else ''))