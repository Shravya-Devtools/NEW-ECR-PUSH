import boto3
import os
import json


def lambda_handler(event, context):
    # 1. Setup the SQS client using the DevOps VPC Endpoint
    sqs = boto3.client(
        'sqs',
        endpoint_url=os.environ['SQS_ENDPOINT_URL'],  # DevOps VPCE DNS
        region_name='us-east-1'
    )

    # 2. Define the message body
    message_body = {
        "status": "success",
        "source": "MerchantLambda",
        "data": "Cron task executed"
    }

    # 3. Send the message to the App Account SQS queue
    response = sqs.send_message(
        QueueUrl=os.environ['SQS_QUEUE_URL'],  # Target App SQS URL
        MessageBody=json.dumps(message_body)
    )

    # 4. Return success response
    return {
        "statusCode": 200,
        "body": f"Message sent! ID: {response['MessageId']}"
    }
