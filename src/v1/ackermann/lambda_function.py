import datetime
import json
import src.common.utils as common_utils
import src.common.response_builder as response_builder

logger = common_utils.get_logger()

SERVICE_NAME = 'KlarnaServerless-Ackermann'


def lambda_handler(event, context):
    try:
        logger.info(event)
        param_m = str(event['queryStringParameters']['m'])
        param_n = str(event['queryStringParameters']['n'])

        # if input is not valid, throw error and return error response
        is_input_valid(param_m, param_n)

        # else Calculate Ackermann
        response_data = get_ackermann_response_data(param_m, param_n)
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


def is_input_valid(input_m=None, input_n=None):
    '''
        Validates if the input is correct
    '''
    if not str(input_m).isdigit() or int(input_m) < 0:
        raise ValueError()
    if not str(input_n).isdigit() or int(input_n) < 0:
        raise ValueError()
    return True


def get_ackermann_response_data(param_m, param_n):
    '''
        Prepares response series along with time consumed
    '''
    start = datetime.datetime.utcnow().timestamp()
    m = int(param_m)
    n = int(param_n)
    ackermann = calculate_ackermann(m, n)
    end = datetime.datetime.utcnow().timestamp()

    # converting the difference to milliseconds
    time_taken = (end - start) * 1000

    response_data = {
        "input": {
            "m": m,
            "n": n
        },
        "ackermann": ackermann,
        "timeTakenMillis": round(time_taken, 3)
    }
    return response_data


def calculate_ackermann(m=0, n=0):
    '''
        Calculates Ackermann of given M, N
    '''
    if m == 0:
        return (n + 1)
    elif n == 0:
        return calculate_ackermann(m - 1, 1)
    else:
        return calculate_ackermann(m - 1, calculate_ackermann(m, n - 1))
