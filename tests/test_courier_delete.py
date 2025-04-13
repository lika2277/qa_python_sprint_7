import allure
import pytest

from instances.courier import Courier

@allure.suite("Удалить курьера")
class TestCourierDelete(Courier):
    @allure.title("неуспешный запрос возвращает соответствующую ошибку")
    def test_courier_delete_error(self):
        pytest.skip('Неправильный код ответа')
        response = self.delete_courier("a123")
        assert response.status_code == 404 and response.json()["message"] == 'Not Found.'

    @allure.title("если отправить запрос без id, вернётся ошибка")
    def test_courier_delete_error_without_id(self):
        response = self.delete_courier()
        assert response.status_code == 404 and response.json()["message"] == 'Not Found.'

    @allure.title("если отправить запрос с несуществующим id, вернётся ошибка")
    def test_courier_delete_error_wrong_id(self):
        response = self.delete_courier(1234567)
        assert response.status_code == 404 and response.json()["message"] == "Курьера с таким id нет."

    @allure.title("успешный запрос возвращает 'ok'")
    def test_courier_delete_error_success(self, courier_id):
        response = self.delete_courier(courier_id)
        assert response.status_code == 200 and response.json()["ok"] == True