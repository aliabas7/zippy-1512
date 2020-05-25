#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto3
import botocore
import click

session = boto3.Session()
ec2 = session.resource("ec2")
client = boto3.client("ec2")


def filter_instances(tag):

    if tag:
        instances = ec2.instances.filter(
            Filters=[{"Name": "tag:tag", "Values": [tag,]}]
        )
    else:
        instances = ec2.instances.all()

    return instances


@click.group("instances")
def instances():
    """A program to manage EC2 Instances - By Ali"""


@instances.command("create")
@click.argument("image_id")
@click.argument("instance_type")
@click.argument("key_name")
def create_instances(image_id, instance_type, key_name):
    """ Create a brand new EC2 instance. """

    instances = ec2.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        KeyName=key_name,
        TagSpecifications=[
            {"ResourceType": "instance", "Tags": [{"Key": "tag", "Value": "boto"},]}
        ],
    )

    instance = instances[0]
    instance.wait_until_running()
    instance.load()
    print(instance.public_ip_address)


@instances.command("list")
@click.option("--tag")
def list_instances(tag, default=None):
    """List instances in your account"""

    instances = filter_instances(tag)

    for i in instances:
        print(i.id, i.state["Name"], i.instance_type)


@instances.command("stop")
@click.option("--tag")
def stop_instances(tag):
    """Stop EC2 instances"""
    instances = filter_instances(tag)

    for i in instances:
        print(f"Stopping instance {i.id}")
        try:
            i.stop()
        except botocore.exceptions.ClientError as e:
            print(f"Could not stop instance: {i.id}.\n" + str(e))
            continue
    return


@instances.command("start")
@click.option("--tag")
def start_instances(tag):
    """Start an EC2 instance"""
    instances = filter_instances(tag)

    for i in instances:
        try:
            i.start()

        except botocore.exceptions.ClientError as e:
            print(f"Could not start instance: {i.id}.\n" + str(e))
            continue
    return


@instances.command("terminate")
@click.option("--tag")
def terminate_instances(tag):
    """Terminate EC2 instances"""

    # confirm if user wants to terminate all instances when tag not specified
    if not tag:
        prompt = (
            "Terminate ALL instances? [Lowercase 'y' for Yes, any other key for No]: "
        )
        user_input = input(prompt)
        if user_input != "y":
            print("Cancelling, no instances terminated")
            raise SystemExit(0)

    instances = filter_instances(tag)

    for i in instances:
        try:
            print(f"Terminating {i.id}")
            i.terminate()
        except botocore.exceptions.ClientError as e:
            print(f"Could not terminate instance: {i.id}.\n" + str(e))
        continue
    return


if __name__ == "__main__":
    instances()
