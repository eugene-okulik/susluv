import requests
import allure

from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    id = None

    @allure.step('Delete Object')
    def delete_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.base_url}/object/{object_id}')
        return self.response
