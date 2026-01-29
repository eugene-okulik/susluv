import requests


def h_create():
    data = {
        "data": {
            "color": "red",
            "size": "medium"
        },
        "name": "elephant"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=data,
        headers=headers
    )
    return response.json()['id']


def h_clear(object_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


def t_get_all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200


def t_get_object_by_id():
    object_id = h_create()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.json()["id"] == object_id
    h_clear(object_id)


def t_post_an_object():
    data = {
        "data": {
            "color": "red",
            "size": "medium"
        },
        "name": "elephant"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=data,
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()['name'] == 'elephant'
    assert response.json()['data']['color'] == 'red'
    assert response.json()['data']['size'] == 'medium'
    h_clear(response.json()['id'])


def t_put_an_object():
    object_id = h_create()
    data = {
        "data": {
            "color": "red-UP",
            "size": "medium-UP"
        },
        "name": "elephant-UP"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=data,
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()['name'] == 'elephant-UP'
    assert response.json()['data']['color'] == 'red-UP'
    assert response.json()['data']['size'] == 'medium-UP'
    h_clear(object_id)


def t_patch_an_object():
    object_id = h_create()
    data = {
        "name": "elephant-UP"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=data,
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()['name'] == 'elephant-UP'
    h_clear(object_id)


def t_delete_an_object():
    object_id = h_create()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200
