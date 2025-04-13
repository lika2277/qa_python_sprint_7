import allure
from instances.courier import Courier

@allure.suite("Создание курьера")
class TestCourierCreate(Courier):

    @allure.title("курьера можно создать и запрос возвращает правильный код ответа и статус 'ok'")
    def test_create_courier(self):
        response = self.register_new_courier(self.generate_new_courier())
        assert response.status_code == 201 and response.json()["ok"] == True

    @allure.title("нельзя создать двух одинаковых курьеров")
    def test_double_create_courier(self):
        courier = self.generate_new_courier()
        first_response = self.register_new_courier(courier)
        second_response = self.register_new_courier(courier)
        assert (first_response.status_code == 201
                and first_response.json()["ok"] == True
                and second_response.status_code == 409
                and second_response.json()["message"] == 'Этот логин уже используется. Попробуйте другой.')

    @allure.title("чтобы создать курьера, нужно передать в ручку все обязательные поля")
    def test_create_courier_data(self):
        courier = self.generate_new_courier()
        del courier['login']
        response = self.register_new_courier(courier)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для создания учетной записи'

    @allure.title("если одного из полей нет, запрос возвращает ошибку")
    def test_create_courier_fields(self):
        courier = self.generate_new_courier()
        del courier['password']
        response = self.register_new_courier(courier)
        assert (response.status_code == 400
            and response.json()["message"] == "Недостаточно данных для создания учетной записи")

    @allure.title("если создать пользователя с логином, который уже есть, возвращается ошибка")
    def test_create_courier_error(self):
        courier = self.generate_new_courier()
        first_response = self.register_new_courier(courier)
        second_response = self.register_new_courier(courier)
        assert (first_response.status_code == 201
            and second_response.status_code == 409
            and second_response.json()["message"] == "Этот логин уже используется. Попробуйте другой.")
