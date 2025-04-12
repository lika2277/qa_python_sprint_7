import allure
from instances.courier import Courier

@allure.title("Удалить курьера")
class TestCourierDelete(Courier):
    @allure.step("неуспешный запрос возвращает соответствующую ошибку")
    def test_courier_delete_error(self):
        response = self.delete_courier("a123")
        assert response.status_code != 200

    @allure.step("если отправить запрос без id, вернётся ошибка")
    def test_courier_delete_error_without_id(self):
        response = self.delete_courier()
        assert response.status_code != 200

    @allure.step("если отправить запрос с несуществующим id, вернётся ошибка")
    def test_courier_delete_error_wrong_id(self):
        response = self.delete_courier(1234567)
        assert response.status_code == 404 and response.json()["message"] == "Курьера с таким id нет."

    @allure.step("успешный запрос возвращает 'ok'")
    def test_courier_delete_error_success(self, courier_id):
        response = self.delete_courier(courier_id)
        assert response.status_code == 200 and response.json()["ok"] == True