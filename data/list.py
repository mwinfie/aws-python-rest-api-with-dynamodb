import json
import os

from data import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    try:
        limit = int(event["queryStringParameters"]['limit'])
    except TypeError:
        limit = int(500)

    # fetch all data from the database
    result = table.scan(Limit=limit)

    #event["queryStringParameters"]['limit'] will be used to access limit Query String

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
