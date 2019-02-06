from twilio.rest import Client
import argparse
import time
import os

parser = argparse.ArgumentParser()
parser.add_argument("--msg", help="message text to be sent")
args = parser.parse_args()

account_sid = os.environ['SID'] 
auth_token = os.environ['TKN'] 
to_num = os.environ['TO_NUM']
from_num = os.environ['FROM_NUM']

client = Client(account_sid, auth_token)

message = client.messages.create(
                to=to_num,
                from_=from_num,
                body=args.msg)
