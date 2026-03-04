import requests
import allure

from endpoints.endpoint import Endpoint


class PatchObject(Endpoint):
    id = None

    @allure.step('Update one field in Object')
    def patch_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.base_url}/object/{object_id}', json=payload, headers=headers)
        self.json = self.response.json()
        self.id = self.json['id']
        return self.response
