#!/bin/bash

AL2="ami-09edd32d9b0990d49"
INSTANCE_TYPE="t3.large"
KEY_NAME="$1"
KEY_PATH="$2"

echo "Creating instance..."

pub_ip=$(/usr/local/bin/python3 /Users/ssyedabb/Desktop/repos/ssyedabb/ssyedabb/ssyedabb.py create "$AL2" "$INSTANCE_TYPE" "$KEY_NAME")

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
