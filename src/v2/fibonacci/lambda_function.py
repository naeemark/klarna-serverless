import datetime
import json
import src.common.utils as common_utils
import src.common.response_builder as response_builder

logger = common_utils.get_logger()

SERVICE_NAME = 'KlarnaServerless-Fibonacci'


def lambda_handler(event, context):
    try:
        logger.info(event)
        param_n = str(event['queryStringParameters']['n'])

        # if input is not valid, throw error and return error response
        is_input_valid(param_n)

        # else Calculate Fibonacci Series
        response_data = get_fibonacci_response_data(param_n)
        response = response_builder.get_success_response(
            status_code=200,
            message=SERVICE_NAME,
            data=response_data
        )
    except (ValueError) as err:
        logger.error(err)
        response = response_builder.get_error_response(status_code=400)
    except (RecursionError) as err:
        logger.error(err)
        response = response_builder.get_error_response(status_code=422)
    except (KeyError, IOError, TimeoutError, Exception) as err:
        logger.error(err)
        response = response_builder.get_error_response()
    return response


def is_input_valid(input=None):
    ''' 
        Validates if the input is correct
        Can also be done by raising an Error
    '''
    if not str(input).isdigit():
        raise ValueError()
    elif int(input) <= 0:
        raise ValueError()
    elif int(input) > 100000:
        raise RecursionError()
    else:
        return True


def get_fibonacci_response_data(param_n):
    ''' 
        Prepares response series along with time constraint values 
    '''
    start = datetime.datetime.utcnow().timestamp()
    n = int(param_n)
    f_of_n = calculate_fibonacci(n)
    end = datetime.datetime.utcnow().timestamp()

    # converting the difference to milliseconds
    time_taken = (end - start) * 1000

    response_data = {
        "n": n,
        "F(n)": f_of_n,
        "timeTakenMillis": round(time_taken, 3)
    }
    return response_data


def calculate_fibonacci(n):
    ''' 
        Calculates Fibonacci Series
        Assumed that the F0 is not required 
    '''
    a, b = 1, 1
    if n == 1 or n == 2:
        return b

    for _ in range(n-2):
        a, b = b, b+a

    return b
