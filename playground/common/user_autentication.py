import boto3

def authenticate_user(headers):
    bearer_token = headers.get('Authorization').split('Bearer ')[1]
    try:
        client = boto3.client('cognito-idp')
        response = client.get_user(
        AccessToken=bearer_token)

    except Exception as e:
        raise Exception(str(e))
    
    return response