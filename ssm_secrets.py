#!/usr/bin/env python3

import boto3

def get_secret(parameter_name):
    """ Get a parameter from SSM parameter store """
    ssm = boto3.client('ssm')
    parameter = ssm.get_parameter(
        Name = parameter_name,
        WithDecryption=True
    )['Parameter']['Value']
    return parameter

def put_secret(parameter_name, parameter_value):
    """ Put a parameter inside SSM parameter store with encrypted
    value"""
    print(f'Putting a parameter with name of {parameter_name}')
    ssm = boto3.client('ssm')
    ssm.put_parameter(
        Name=parameter_name,
        Value=parameter_value,
        Type='SecureString',
        Overwrite=True
    )
    print(f'Successfully added a parameter with name {parameter_name}')

    #Example of using put_secret()
    SECRETS = {
        "CONSUMER_KEY": "<replace_me>",
        "CONSUMER_SECRET": "<replace_me>",
        "ACCESS_TOKEN_KEY": "<replace_me>",
        "ACCESS_TOKEN_SECRET": "<replace_me>"
    }

    for parameter_name, parameter_value in SECRETS.items():
        put_secret(parameter_name, parameter_value)

