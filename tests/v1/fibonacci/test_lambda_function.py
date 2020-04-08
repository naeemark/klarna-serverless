from nose.tools import *
from src.v1.fibonacci.lambda_function import lambda_handler, is_input_valid, calculate_fibonacci


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
    is_input_valid(0)


def test_is_input_valid_true():
    flag = is_input_valid(5)
    assert flag is True


def test_calculate_fibonacci_for_1():
    n = 1
    series = calculate_fibonacci(n)
    assert len(series) == n
    assert series[0] == 1


def test_calculate_fibonacci_for_2():
    n = 2
    series = calculate_fibonacci(n)
    assert len(series) == n
    assert series[0] == 1
    assert series[1] == 1


def test_calculate_fibonacci_for_5():
    n = 5
    expected_series = [1, 1, 2, 3, 5]
    series = calculate_fibonacci(n)
    assert len(series) == len(expected_series)
    assert series == expected_series
