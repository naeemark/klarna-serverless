from nose.tools import *
from src.v1.ackermann.lambda_function import lambda_handler, is_input_valid, calculate_ackermann


def test_lambda_handler_400():
    event = {'queryStringParameters': {'m': None, 'n': None}}
    response = lambda_handler(event, None)
    assert response is not None
    assert response['statusCode'] == 400


@raises(Exception)
def test_lambda_handler_500():
    event = {'queryStringParameters': {'m': 1, 'n': 1}}
    response = lambda_handler(event, None)
    assert response is not None
    assert response['statusCode'] == 500


@raises(ValueError)
def test_is_input_valid_false():
    is_input_valid(-1, 0)


@raises(ValueError)
def test_is_input_valid_false():
    is_input_valid(1, "-5")


def test_is_input_valid_true():
    flag = is_input_valid(5, 1)
    assert flag is True


def test_calculate_ackermann_for_0_0():
    m, n = 0, 0
    ackermann = calculate_ackermann(m, n)
    assert ackermann == 1


def test_calculate_ackermann_for_1_1():
    m, n = 1, 1
    ackermann = calculate_ackermann(m, n)
    assert ackermann == 3


def test_calculate_ackermann_for_2_2():
    m, n = 2, 2
    ackermann = calculate_ackermann(m, n)
    assert ackermann == 7


@raises(RecursionError)
def test_calculate_ackermann_for_5_5():
    m, n = 5, 5
    ackermann = calculate_ackermann(m, n)
