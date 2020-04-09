from nose.tools import *
from src.v2.fibonacci.lambda_function import lambda_handler, is_input_valid, calculate_fibonacci


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
def test_is_input_valid_false_0():
    is_input_valid(0)


@raises(RecursionError)
def test_is_input_valid_false_max():
    is_input_valid(100001)


def test_is_input_valid_true():
    flag = is_input_valid(5)
    assert flag is True


def test_calculate_fibonacci_for_1():
    n = 1
    f = calculate_fibonacci(n)
    assert f == 1


def test_calculate_fibonacci_for_2():
    n = 2
    f = calculate_fibonacci(n)
    assert f == 1


def test_calculate_fibonacci_for_5():
    n = 5
    expected_f = 5
    f = calculate_fibonacci(n)
    assert f == expected_f


def test_calculate_fibonacci_for_9():
    n = 9
    expected_f = 34
    f = calculate_fibonacci(n)
    assert f == expected_f
