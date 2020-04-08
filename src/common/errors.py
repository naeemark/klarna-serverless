import json

error_default = {
    'statusCode': 500,
    'body': json.dumps({
        'responseCode': 500,
        'responseMessage': 'Something bad happened!',
        'response': {
            'errors': {
                'errorCode': 'UNCAUGHT',
                'errorTitle': 'We seem to have a problem!',
                'errorDescription': 'Our internal system is having problem, please contact our administrator!'
            }
        }
    })
}

error_not_found_404 = {
    'statusCode': 404,
    'body': json.dumps({
        'responseCode': 404,
        'responseMessage': 'Resource not found',
        'response': {
            'errors': {
                'errorCode': 'NOT_FOUND',
                'errorTitle': 'Resource not found',
                'errorDescription': 'Seems the object which you are trying to find is not available'
            }
        }
    })
}

error_bad_request_400 = {
    'statusCode': 400,
    'body': json.dumps({
        'responseCode': 400,
        'responseMessage': 'Invalid Params',
        'response': {
            'error': {
                'errorCode': 'VALIDATION_ERROR',
                'errorTitle': 'Invalid Parameters provided',
                'errorDescription': 'Seems the provided input is not validated by the system'
            }
        }
    })
}

error_unprocessable_422 = {
    'statusCode': 422,
    'body': json.dumps({
        'responseCode': 422,
        'responseMessage': 'UNPROCESSABLE ENTITY',
        'response': {
            'error': {
                'errorCode': 'UNPROCESSABLE_ENTITY',
                'errorTitle': 'Too much processing required',
                'errorDescription': 'Seems that maximum recursion depth exceeded in comparison. Please use lower values i.e m=2, n=2'
            }
        }
    })
}


def get_error(status_code):
    errors = {
        400: error_bad_request_400,
        404: error_not_found_404,
        422: error_unprocessable_422,
    }
    if status_code in errors:
        return errors.get(status_code)
    else:
        return error_default
