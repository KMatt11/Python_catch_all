## Script to create Standard SQS Queue

import boto3

## Get the service resource
sqs = boto3.resource('sqs')

## Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='kinsey-queue')

## You can now access identifiers and attributes
print(queue.url)