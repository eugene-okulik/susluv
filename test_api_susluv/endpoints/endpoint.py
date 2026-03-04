import allure


class Endpoint:
    base_url = 'http://objapi.course.qa-practice.com'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that response content is correct')
    def check_response_content_is_correct(self, data):
        assert self.json['data'] == data['data']
        assert self.json['name'] == data['name']

    @allure.step('Check that response data is correct')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name

    @allure.step('Check that response id is correct')
    def check_response_id_is_correct(self, object_id):
        assert self.json['id'] == object_id

    @allure.step('Check that response status is correct')
    def check_status(self, status=200):
        assert self.response.status_code == status
