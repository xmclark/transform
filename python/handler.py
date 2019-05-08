
import json
import datetime


def endpoint(event, context):
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello Ronny, time is " + str(current_time)
    }

    response = {
        "body": json.dumps(body)
    }

    return response