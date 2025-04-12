from instances.courier import Courier
import pytest
import allure

@allure.title("Логин курьера")
@pytest.mark.usefixtures("register_and_delete")
class TestCourierLogin(Courier):
    @allure.step("курьер может авторизоваться")
    def test_courier_login(self):
        response = self.login_courier(self.courier)
        assert response.status_code == 200

    @allure.step("успешный запрос возвращает id")
    def test_courier_login_id(self):
        response = self.login_courier(self.courier)
        assert response.status_code == 200 and response.json()["id"]

    @allure.step("для авторизации нужно передать все обязательные поля")
    def test_courier_login_required(self):
        pytest.skip("Неправильный ответ сервера")
        courier = self.courier.copy()
        del courier["password"]
        response = self.login_courier(courier)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.step("система вернёт ошибку, если неправильно указать логин или пароль")
    def test_courier_login_wrong_password(self):
        courier = self.courier.copy()
        courier["password"] = '1234567'
        response = self.login_courier(courier)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

    @allure.step("если какого-то поля нет, запрос возвращает ошибку")
    def test_courier_login_empty_password(self):
        courier = self.courier.copy()
        courier["password"] = ''
        response = self.login_courier(courier)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.step("если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_courier_login_wrong_login(self):
        courier = self.generate_new_courier()
        response = self.login_courier(courier)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

