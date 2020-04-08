import datetime
import json
import src.common.utils as common_utils
import src.common.response_builder as response_builder

logger = common_utils.get_logger()


def lambda_handler(event, context):
    try:
        logger.info(event)
        param_n = str(event['queryStringParameters']['n'])

        # if input is not valid, return error response
        if not is_input_valid(param_n):
            response = response_builder.get_error_response(status_code=400)
        # Calculate Fibonacci Series
        else:
            response_data = get_fibonacci_response_data(param_n)
            response = response_builder.get_success_response(
                status_code=200,
                message='Fibonacci Series',
                data=response_data
            )
    except (IOError, ValueError, KeyError, TimeoutError, Exception) as err:
        logger.error(err)
        response = response_builder.get_error_response()
    return response


def is_input_valid(input=None):
    ''' 
        Validates if the input is correct
        Can also be done by raising an Error
    '''
    if not str(input).isdigit():
        return False
    elif int(input) <= 0:
        return False
    else:
        return True


def get_fibonacci_response_data(param_n):
    ''' 
        Prepares response series along with time constraint values 
    '''
    start = datetime.datetime.utcnow().timestamp()
    n = int(param_n)
    series = calculate_fibonacci(n)
    end = datetime.datetime.utcnow().timestamp()

    # converting the difference to milliseconds
    time_taken = (end - start) * 1000

    response_data = {
        "n": n,
        "fibonacciSeries": series,
        "totalElements": len(series),
        "timeTakenMillis": round(time_taken, 3)
    }
    return response_data


def calculate_fibonacci(n):
    ''' 
        Calculates Fibonacci Series
        Assumed that the F0 is not required 
    '''
    a, b = 1, 1
    fibs = [a, b]
    if n == 1:
        return [1]
    if n == 2:
        return fibs

    for _ in range(n-2):
        a, b = b, b+a
        fibs.append(b)

    return fibs
