from src.common.response_builder import get_default_response


def test_get_default_response_success():
    response = get_default_response()
    assert response is not None
    assert response['statusCode'] == 200
