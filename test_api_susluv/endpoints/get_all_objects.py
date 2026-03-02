import requests
import allure

from endpoints.endpoint import Endpoint


class GetAllObjects(Endpoint):
    id = None

    @allure.step('Get all Objects')
    def get_all_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.base_url}/object', headers=headers)
        if self.response.status_code == 200:
            self.json = self.response.json()
        return self.response
