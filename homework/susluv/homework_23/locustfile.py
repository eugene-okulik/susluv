from locust import task, HttpUser, between
import random


class RegularUser(HttpUser):
    weight = 10
    wait_time = between(1, 5)
    ids_for_get = []

    def on_start(self):
        for i in range(3):
            response = self.client.post(
                '/object',
                json={"data": {"color": "green", "size": "big"}, "name": "diplodocus"},
                headers={'Content-Type': 'application/json'}
            )
            self.ids_for_get.append(response.json()['id'])

    def on_stop(self):
        for i in self.ids_for_get:
            response = self.client.delete(f'/object/{i}')

    @task(1)
    def get_all_objects(self):
        self.client.get(
            '/object'
        )

    @task(10)
    def get_one_object(self):
        self.client.get(
            f'/object/{random.choice(self.ids_for_get)}'
        )


class AdminUser(HttpUser):
    weight = 1
    wait_time = between(1, 5)

    @task
    def do_admin_things(self):
        post_response = self.client.post(
            '/object',
            json={"data": {"color": "green", "size": "big"}, "name": "diplodocus"},
            headers={'Content-Type': 'application/json'}
        )
        self.client.put(
            f"/object/{post_response.json()['id']}",
            json={"data": {"color": "green-UP", "size": "big-UP"}, "name": "diplodocus-UP"},
            headers={'Content-Type': 'application/json'}
        )
        self.client.delete(f'/object/{post_response.json()['id']}')
