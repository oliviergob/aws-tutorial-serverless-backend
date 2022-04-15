import boto3
import yaml
import json
import os


S3_BUCKET = os.environ['S3_BUCKET']
CONFIG_FILE = 'config.yaml'

def handler(event, context):

    # Getting config file from S3 bucket
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=S3_BUCKET, Key=CONFIG_FILE)

    # Parsing response file
    configfile = yaml.safe_load(response["Body"])
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS'
        },
        'body': json.dumps(configfile)
    }


