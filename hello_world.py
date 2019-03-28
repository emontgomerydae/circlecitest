import boto3
import datetime
import logging
import os
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    stage = os.environ['Stage']
    region = os.environ['Region']
    lambdaResponse = True

    logger.info('{}: {}: Hello world!'.format(region, stage))
    
    return lambdaResponse 