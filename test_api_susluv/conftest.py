import pytest
from endpoints.create_object import CreateObject
from endpoints.get_all_objects import GetAllObjects
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.patch_object import PatchObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def get_all_objects_endpoint():
    return GetAllObjects()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def new_object_id(create_object_endpoint, delete_object_endpoint):
    data = {"data": {"color": "red", "size": "medium"}, "name": "elephant"}
    create_object_endpoint.create_new_object(data)
    yield create_object_endpoint.id
    delete_object_endpoint.delete_object(create_object_endpoint.id)
