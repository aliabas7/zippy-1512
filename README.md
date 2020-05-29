# zippy-1512

Manage your EC2 instances from CLI with Zippy. 

##Description

This is a python program that uses boto3 to let you create, start, list, stop and terminate Amazon EC2 instances from CLI. The program uses credentials configured in your aws profile.

## Prerequisites

  - Python 3.4, or a later version
  - AWS Profile configured which must have a default region 

## Installation

    pip3 install https://ali-spython-stuff.s3.amazonaws.com/zippy_1512-0.1-py3-none-any.whl --upgrade --user 

## Running

            zippy --help 
            zippy COMMAND [ARGS]
            zippy create image_id instance_type key_name
            zippy list --tag tag_value
            zippy start --tag tag_value
            zippy stop --tag tag_value
            zippy terminate --tag tag_value

*Notes:*

tag is optional
To make managing them simple, instances created with zippy have a default tag of TagName: tag and TagValue: boto. So, if you just want to terminate instnaces created with zippy, you can run below command:

            zippy terminate --tag boto

## Wrapper script

To create an instance, you can run zippy create command, however, it's recommended to use the wrapper.sh script. 

The bash script lets you create a new instance and ssh into it with a single command from terminal. It requires two arguments, the first one must be the name of the ssh key in your AWS account and the second must be the location of the ssh key on your machine. It creates an EC2 instance using the AL2 (us-east-1) and creates a t3.large instance.

Usage:

            ./wrapper.sh mykey ~/.ssh/mykey.pem

You can edit the variables (AL2, INSTANCE_TYPE, and also hard code the value for SSH_KEY) to further customize the wrapper.

*Windows users:*

Either user WSL or go get yourself a mac.

## Uninstalling zippy
          
          pip3 uninstall zippy-1512