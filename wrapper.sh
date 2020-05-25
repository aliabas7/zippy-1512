#!/bin/bash

AMI="ami-09edd32d9b0990d49" #Amazon Linux 2 for us-east-1, please update this value
INSTANCE_TYPE="t3.large"
KEY_NAME="$1" #Key name in your aws account, hardcode the key if you use the same key
KEY_PATH="$2" #Full path to the key on your local machine, hardcode the key if you use the same key

if [ "$KEY_NAME" = "" ] || [ "$KEY_PATH" = "" ]; then
    echo "Please enter key name and full path to the key on your local machine:"
    echo "./wrapper.sh keyname /keypath"
    exit 1
fi

echo "Creating instance..."

pub_ip=$(/usr/local/bin/python3 /Users/ssyedabb/Desktop/repos/zippy/zippy/zippy.py create "$AMI" "$INSTANCE_TYPE" "$KEY_NAME")

if [ "$pub_ip" = "" ]; then
    echo "Something went wrong, see above error"
    exit 1
fi

echo "Instance created, sshing..."

while true; do
    if ssh -i "$KEY_PATH" "ec2-user@$pub_ip"; then
        exit 0
    else
        echo "Instance not ready. Retrying..."
        sleep 3
        continue
    fi
done
