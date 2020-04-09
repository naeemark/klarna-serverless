import datetime
import math
import json
import src.common.utils as common_utils
import src.common.response_builder as response_builder

logger = common_utils.get_logger()

SERVICE_NAME = 'KlarnaServerless-Factorial'


def lambda_handler(event, context):
    try:
        logger.info(event)
        param_n = str(event['queryStringParameters']['n'])

        # if input is not valid, throw error and return error response
        is_input_valid(param_n)

        # else Calculate Factorial
        response_data = get_factorial_response_data(param_n)
        response = response_builder.get_success_response(
            status_code=200,
            message=SERVICE_NAME,
            data=response_data
        )
    except (ValueError) as err:
        logger.error(err)
        response = response_builder.get_error_response(status_code=400)
    except (KeyError, IOError, TimeoutError, Exception) as err:
        logger.error(err)
        response = response_builder.get_error_response()
    return response


def is_input_valid(input=None):
    ''' 
        Validates if the input is correct
    '''
    if not str(input).isdigit() or int(input) < 0:
        raise ValueError()
    else:
        return True


def get_factorial_response_data(param_n):
    ''' 
        Prepares response series along with time consumed
    '''
    start = datetime.datetime.utcnow().timestamp()
    n = int(param_n)
    factorial = calculate_factorial(n)
    end = datetime.datetime.utcnow().timestamp()

    # converting the difference to milliseconds
    time_taken = (end - start) * 1000

    response_data = {
        "n": n,
        "factorial": factorial,
        "timeTakenMillis": round(time_taken, 3)
    }
    return response_data


def calculate_factorial(n):
    ''' 
        Calculates Factorial of given N i.e:
        n!= n x (n-1) x (n-2) x (n-3) x ... x 3 x 2 x 1
        Using Python math package
    '''
    return math.factorial(n)
