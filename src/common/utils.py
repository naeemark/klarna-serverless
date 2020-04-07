import logging
import json


def get_logger(logger_name='KlarnaServerless'):
    log = logging.getLogger(logger_name)
    log.setLevel(logging.DEBUG)
    return log
