import requests
import allure

from endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):
    id = None

    @allure.step('Update new Object')
    def update_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.base_url}/object/{object_id}', json=payload, headers=headers)
        self.json = self.response.json()
        self.id = self.json['id']
        return self.response
