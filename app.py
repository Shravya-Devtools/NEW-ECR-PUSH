import boto3
import os
 
def lambda_handler(event, context):
    print("Step 1: Starting SQS test...")
    # We leave the endpoint_url EMPTY. 
    # This forces Lambda to try the public internet (which is blocked).
    sqs = boto3.client('sqs', region_name='us-east-1')
    try:
        print("Step 2: Attempting to reach public SQS...")
        sqs.send_message(
            QueueUrl=os.environ.get('SQS_QUEUE_URL'),
            MessageBody="This message should never arrive."
        )
        return {"status": "SUCCESS", "message": "Unexpectedly reached SQS!"}
    except Exception as e:
        print(f"Step 3: Failed as expected! Error: {str(e)}")
        return {"status": "FAILED", "error": str(e)}
