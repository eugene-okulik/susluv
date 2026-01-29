import requests
import pytest


@pytest.fixture()
def new_object_id():
    data = {"data": {"color": "red", "size": "medium"}, "name": "elephant"}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=data, headers=headers)
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.fixture(scope='session', autouse=True)
def outer_session_text():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function', autouse=True)
def outer_test_text():
    print('before test')
    yield
    print('after test')


def test_get_all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200


@pytest.mark.medium
def test_get_object_by_id(new_object_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    assert response.json()["id"] == new_object_id


@pytest.mark.parametrize('data', [{"data": {"color": "red", "size": "medium"}, "name": "elephant"},
                                  {"data": {"color": "blue", "size": "small"}, "name": "rabbit"},
                                  {"data": {"color": "green", "size": "big"}, "name": "diplodocus"}])
def test_post_an_object(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=data, headers=headers)
    assert response.status_code == 200
    assert response.json()['name'] == data['name']
    assert response.json()['data']['color'] == data['data']['color']
    assert response.json()['data']['size'] == data['data']['size']
    requests.delete(f'http://objapi.course.qa-practice.com/object/{response.json()['id']}')


@pytest.mark.critical
def test_put_an_object(new_object_id):
    data = {"data": {"color": "red-UP", "size": "medium-UP"}, "name": "elephant-UP"}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{new_object_id}',
                            json=data,
                            headers=headers)
    assert response.status_code == 200
    assert response.json()['name'] == 'elephant-UP'
    assert response.json()['data']['color'] == 'red-UP'
    assert response.json()['data']['size'] == 'medium-UP'


def test_patch_an_object(new_object_id):
    data = {"name": "elephant-UP"}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{new_object_id}',
                              json=data,
                              headers=headers)
    assert response.status_code == 200
    assert response.json()['name'] == 'elephant-UP'


def test_delete_an_object(new_object_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    assert response.status_code == 200
