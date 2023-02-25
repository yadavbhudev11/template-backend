from playground.event.event_map import invoke_resource
from playground.common.user_autentication import authenticate_user
import json


def call_event(event):
    event_data = extract_event_details(event)
    user = authenticate_user(event_data['headers'])
    event_data['email'] = user.get('Username')
    resource_respone = call_resource(event_data)
    return resource_respone


def extract_event_details(event):

    event_data = {}
    event_data['resource_path'] = event.get('resource')
    event_data['resource_method'] = event.get('httpMethod')
    event_data['query_params'] = event.get('queryStringParameters')
    event_data['path_params'] = event.get('pathParameters')
    event_data['headers'] = event.get('headers')
    if event.get('body') != None:
        event_data['body'] = json.loads(event.get('body'))
    else:
        event_data['body'] = {}
    return event_data


def call_resource(event_data):
    return invoke_resource(event_data)
