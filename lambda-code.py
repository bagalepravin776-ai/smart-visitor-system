import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Visitors')

sns = boto3.client('sns')

TOPIC_ARN = "arn:aws:sns:ap-south-1:303417979634:VisitorNotification"

def lambda_handler(event, context):

    body = json.loads(event['body'])

    name = body['name']
    email = body['email']
    phone = body['phone']
    purpose = body['purpose']

    table.put_item(
        Item={
            'email': email,
            'name': name,
            'phone': phone,
            'purpose': purpose
        }
    )

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject='New Visitor',
        Message=f'{name} is visiting for {purpose}'
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message':'Visitor Registered Successfully'
        })
    }
