import requests
import allure

from endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    id = None

    @allure.step('Get Object by id')
    def get_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.base_url}/object/{object_id}', headers=headers)
        self.json = self.response.json()
        self.id = self.json['id']
        return self.response
