**zippy-1512 - A program manage your EC2 instances from CLI**

Manage your EC2 instances from CLI with Zippy. 

**Description**

This is a python program that uses boto3 to let you create, start, list, stop and terminate Amazon EC2 instances from CLI. The program uses credentials configured in your aws profile.

**Installation**

pip3 install s3/zippy-1512 (Link will be available soon)

**Running**
zippy --help 
zippy [OPTIONS] COMMAND [ARGS]
zippy create image_id instance_type key_name
zippy list --tag tag_value
zippy start --tag tag_value
zippy stop --tag tag_value
zippy terminate --tag tag_value

**Using Wrapper script**
To create an instance, you can run zippy create command, however, it's recommended to use the wrapper.sh script included in this repo. 

The script lets you create a new instance and ssh into it with a single command. It requires two arguments, the first one must be the name of the ssh key in your AWS account and the second one is the location of the ssh key on your machine. It creates an EC2 instance using the AL2 (us-east-1) and creates a t3.large instance.

Example usage

./wrapper mykey ~/.ssh/mykey.pem

You can edit the variables (AL2, INSTANCE_TYPE, and also hard code the value for SSH_KEY) to further customize the wrapper.
