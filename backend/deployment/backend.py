import os

import boto3

import zipfile

def deploy_lambda():

    # Create a Lambda client

    lambda_client = boto3.client('lambda')

    # Get the Lambda function name

    function_name = os.environ['LAMBDA_FUNCTION_NAME']

    # Get the Lambda function code

    code = lambda_client.get_function(FunctionName=function_name)['Code']['S3Bucket'], lambda_client.get_function(FunctionName=function_name)['Code']['S3ObjectKey']

    # Create a Lambda execution role

    iam_client = boto3.client('iam')

    execution_role = iam_client.create_role(RoleName=function_name, AssumeRolePolicyDocument={'Version': '2012-10-17', 'Statement': [{'Effect': 'Allow', 'Principal': {'Service': 'lambda.amazonaws.com'}, 'Action': 'sts:AssumeRole'}]})['Role']['Arn']

    # Create a Lambda function

    lambda_client.create_function(FunctionName=function_name, Runtime='python3.9', Handler='index.handler', Role=execution_role, Code={'S3Bucket': code[0], 'S3ObjectKey': code[1]})

    return {'status': 'success'}

def main():

    # Deploy the Lambda function

    result = deploy_lambda()

    print(result)

if __name__ == '__main__':

    main()