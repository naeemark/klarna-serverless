from nose.tools import *
from src.v1.factorial.lambda_function import lambda_handler, is_input_valid, calculate_factorial


def test_lambda_handler_400():
    event = {'queryStringParameters': {'n': None}}
    response = lambda_handler(event, None)
    assert response is not None
    assert response['statusCode'] == 400


@raises(Exception)
def test_lambda_handler_500():
    event = {'queryStringParameters': {'n': 20}}
    response = lambda_handler(event, None)
    assert response is not None
    assert response['statusCode'] == 500


@raises(ValueError)
def test_is_input_valid_false():
    is_input_valid(-1)


@raises(ValueError)
def test_is_input_valid_false():
    is_input_valid("-5")


def test_is_input_valid_true():
    flag = is_input_valid(5)
    assert flag is True


def test_calculate_factorial_for_0():
    n = 0
    factorial = calculate_factorial(n)
    assert factorial == 1


def test_calculate_factorial_for_1():
    n = 1
    factorial = calculate_factorial(n)
    assert factorial == 1


def test_calculate_factorial_for_2():
    n = 2
    factorial = calculate_factorial(n)
    assert factorial == 2


def test_calculate_factorial_for_5():
    n = 5
    factorial = calculate_factorial(n)
    assert factorial == 120
