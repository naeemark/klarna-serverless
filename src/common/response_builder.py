import json
from src.common.errors import get_error


response_headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',  # Required for CORS support to work
    'Access-Control-Allow-Credentials': True  # Required for cookies, authorization headers with HTTPS
}


def get_default_response():
    return get_success_response(data={'Result': 'OK'})


def get_success_response(status_code=200, message='Success', data=None):
    return {
        'statusCode': status_code,
        'headers': response_headers,
        'body': json.dumps({
            'responseCode': 200,
            'responseMessage': message,
            'response': data
        })
    }


def get_error_response(status_code=500):
    error_response = get_error(status_code)
    error_response['headers'] = response_headers
    return error_response
