import os

import json

def handler(event, context):

    # Process the event

    print(json.dumps(event))

    return {'status': 'success'}

if __name__ == '__main__':

    handler({}, {})