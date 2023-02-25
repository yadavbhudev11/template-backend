import json
from playground.common.dynamo_converter import DecimalEncoder
from playground.event.event_handler import call_event


def lambda_handler(event, context):
    try:
        response = call_event(event)
    except Exception as e:
        return {
        'statusCode': 500,
        'body': json.dumps({"error":str(e)}),
         'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
            },
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(response, cls=DecimalEncoder),
         'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
            },
    }
