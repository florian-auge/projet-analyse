import boto3
import os

#initialize the ec2 client outside of the handler
ec2 = boto3.client('ec2')
#define the instance id from the variable environments
instance_id = os.environ['INSTANCE_ID']

def lambda_handler(event, context):
    """
    Main Lambda handler function
    Parameters: 
        event:  Dict containing the Lambda function event data
        context: Lambda runtime context
    Returns:
        Dict containing status message
    """

    ec2.stop_instances(InstanceIds= [instance_id])
    return {
        'statusCode': 200,
        'body': 'Instance stopped'
    }