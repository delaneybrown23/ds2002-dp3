import boto3
from botocore.exceptions import ClientError
import requests
import json

# Set up your SQS queue URL and boto3 client
url = "https://sqs.us-east-1.amazonaws.com/440848399208/vvz2bg"
sqs = boto3.client('sqs')

# Loop through all 10 messages in queue with for loop

for i in range(10):
    def delete_message(handle):
        try:
            # Delete message from SQS queue
            sqs.delete_message(
                QueueUrl=url,
                ReceiptHandle=handle
            )
            print("Message deleted")
        except ClientError as e:
            print(e.response['Error']['Message'])

    def get_message():
        try:
            # Receive message from SQS queue. Each message has two MessageAttributes: order and word
            # You want to extract these two attributes to reassemble the message
            response = sqs.receive_message(
                QueueUrl=url,
                AttributeNames=[
                    'All'
                ],
                MaxNumberOfMessages=1,
                MessageAttributeNames=[
                    'All'
                ]
            )
            # Check if there is a message in the queue or not
            if "Messages" in response:
                # extract the two message attributes you want to use as variables
                # extract the handle for deletion later
                order = response['Messages'][0]['MessageAttributes']['order']['StringValue']
                word = response['Messages'][0]['MessageAttributes']['word']['StringValue']
                handle = response['Messages'][0]['ReceiptHandle']

                # Print the message attributes - this is what you want to work with to reassemble the message
                print(f"Order: {order}")
                print(f"Word: {word}")

                # Storing the word and order values as a dictionary pair
                message_dictionary = [{"order": order, "word": word}]

            # If there is no message in the queue, print a message and exit    
            else:
                print("No message in the queue")
                exit(1)
                
        # Handle any errors that may occur connecting to SQS
        except ClientError as e:
            print(e.response['Error']['Message'])

    # increment i each iteration through the for loop
    i = i + 1

# Trigger the function
if __name__ == "__main__":
    get_message()

# Trying to print out the correctly ordered phrase

for each in message_dictionary:
    if order == 0:
        print(word)
    if order == 1:
        print(word)
    if order == 2:
        print(word)
    if order == 3:
        print(word)
    if order == 4:
        print(word)
    if order == 5:
        print(word)
    else if order == 6:
        print(word)
    if order == 7:
        print(word)
    if order == 8:
        print(word)
    if order == 9:
        print(word)
    if order == 10:
        print(word)
    else:
        exit
    
# I continue to get a message in the terminal when trying to run my python script that there is "No message in the queue." I am not sure
# why this error keeps happening, but my code attempts to loop through all 10 messages, store the word and order values in a dictionary, print
# out the correctly reassembled message, and deletes all messages at the end. Unfortunately, I was not able to successfully output the correctly
# reassembled message.
