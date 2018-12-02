# Imports the Google Cloud client library
import os
from google.cloud import logging
from google.cloud import error_reporting
import google.auth as auth
import logging as warn


def write_log(username, password, severity):
    logging_client = logging.Client()

    logger = logging_client.logger('test')
    logger.log_text("A simple entry")

    struct = {
        'username': username,
        'password': password
    }

    logger.log_text('Goodbye, world!', severity='ERROR')
    logger.log_struct(struct, severity=severity)

    if severity == "ERROR":
        client = error_reporting.Client()
        text = "Uncorrect username or password. \nUsername:" + username + "\nPassword:"+password
        client.report(text)
        print(text)

