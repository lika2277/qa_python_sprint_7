import allure
from instances.courier import Courier

@allure.title("Создание курьера")
class TestCourierCreate(Courier):

    @allure.step("курьера можно создать")
    def test_create_courier(self):
        response = self.register_new_courier(self.generate_new_courier())
        assert response.status_code == 201

    @allure.step("нельзя создать двух одинаковых курьеров")
    def test_double_create_courier(self):
        courier = self.generate_new_courier()
        first_response = self.register_new_courier(courier)
        second_response = self.register_new_courier(courier)
        assert first_response.status_code == 201 and not second_response.status_code == 201

    @allure.step("чтобы создать курьера, нужно передать в ручку все обязательные поля")
    def test_create_courier_data(self):
        courier = self.generate_new_courier()
        del courier['login']
        response = self.register_new_courier(courier)
        assert not response.status_code == 201

    @allure.step("запрос возвращает правильный код ответа")
    def test_create_courier_code(self):
        response = self.register_new_courier(self.generate_new_courier())
        assert response.status_code == 201

    @allure.step("успешный запрос возвращает статус 'ok'")
    def test_create_courier_response(self):
        response = self.register_new_courier(self.generate_new_courier())
        print(response.json())
        assert response.json() == {"ok": True}

    @allure.step("если одного из полей нет, запрос возвращает ошибку")
    def test_create_courier_fields(self):
        courier = self.generate_new_courier()
        del courier['password']
        response = self.register_new_courier(courier)
        assert (response.status_code == 400
            and response.json()["message"] == "Недостаточно данных для создания учетной записи")

    @allure.step("если создать пользователя с логином, который уже есть, возвращается ошибка")
    def test_create_courier_error(self):
        courier = self.generate_new_courier()
        first_response = self.register_new_courier(courier)
        second_response = self.register_new_courier(courier)
        assert (first_response.status_code == 201
            and second_response.status_code == 409
            and second_response.json()["message"] == "Этот логин уже используется. Попробуйте другой.")
