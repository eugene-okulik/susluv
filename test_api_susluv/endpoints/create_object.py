import requests
import allure

from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    id = None

    @allure.step('Create new Object')
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.base_url}/object', json=payload, headers=headers)
        if self.response.status_code == 200:
            self.json = self.response.json()
            self.id = self.json['id']
        return self.response
