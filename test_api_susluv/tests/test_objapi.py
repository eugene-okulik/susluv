import pytest


TESTDATA_POSITIVE_CREATE = [{"data": {"color": "red", "size": "medium"}, "name": "elephant"},
                            {"data": {"color": "blue", "size": "small"}, "name": "rabbit"},
                            {"data": {"color": "green", "size": "big"}, "name": "diplodocus"}]

TESTDATA_NEGATIVE_CREATE = [{"data": {"color": "green", "size": "big"}}]

TESTDATA_POSITIVE_UPDATE = [{"data": {"color": "red-UP", "size": "medium-UP"}, "name": "elephant-UP"},
                            {"data": {"color": "red", "size": "medium"}, "name": "elephant-UP"}]


def test_get_all_objects(get_all_objects_endpoint):
    get_all_objects_endpoint.get_all_objects()
    get_all_objects_endpoint.check_status()


@pytest.mark.medium
def test_get_object_by_id(get_object_endpoint, new_object_id):
    get_object_endpoint.get_object(object_id=new_object_id)
    get_object_endpoint.check_status()
    get_object_endpoint.check_response_id_is_correct(new_object_id)


@pytest.mark.parametrize('data', TESTDATA_POSITIVE_CREATE)
def test_post_an_object_pos(create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_status()
    create_object_endpoint.check_response_content_is_correct(data)


@pytest.mark.parametrize('data', TESTDATA_NEGATIVE_CREATE)
def test_post_an_object_neg(create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_status(400)


@pytest.mark.critical
@pytest.mark.parametrize('data', TESTDATA_POSITIVE_UPDATE)
def test_put_an_object_pos(update_object_endpoint, new_object_id, data):
    update_object_endpoint.update_object(object_id=new_object_id, payload=data)
    update_object_endpoint.check_status()
    update_object_endpoint.check_response_content_is_correct(data)


def test_patch_an_object(patch_object_endpoint, new_object_id):
    data = {"name": "elephant-UP"}
    patch_object_endpoint.patch_object(object_id=new_object_id, payload=data)
    patch_object_endpoint.check_status()
    patch_object_endpoint.check_response_name_is_correct(data['name'])


def test_delete_an_object(delete_object_endpoint, new_object_id):
    delete_object_endpoint.delete_object(object_id=new_object_id)
    delete_object_endpoint.check_status()
