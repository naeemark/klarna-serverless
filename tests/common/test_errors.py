from src.common.errors import get_error


def test_get_error():
    error = get_error(None)
    assert error is not None


def test_get_error_400():
    error = get_error(400)
    assert error is not None
    assert error['statusCode'] == 400


def test_get_error_404():
    error = get_error(404)
    assert error is not None
    assert error['statusCode'] == 404