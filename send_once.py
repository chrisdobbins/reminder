import subprocess
import subprocess
import time
import datetime
import re
import os
import shlex
import argparse
from dateutil import parser
import string

def send (msg):
    formatted_msg = msg["msg"].replace(" ", "\ ")
    at_proc = subprocess.Popen(['at', msg["date"]], stdin=subprocess.PIPE, shell=False)
    send_proc = subprocess.Popen(shlex.split('/bin/echo python3 ' + os.environ['PWD'] + '/msg-sender.py --msg "' + formatted_msg + '"'), stdout=at_proc.stdin, shell=False)
    at_proc.communicate()
    return

def process_input(time_msg):
    time_pattern = re.compile('at (\d{1,2}:\d{2})')
    time_result = time_pattern.match(time_msg)

    if time_result is None:
        print('invalid time')
        return

    msg_time = parser.parse(time_result.group(1))
    if msg_time is None:
        print('invalid time')
        return

    formatted_time = msg_time.strftime('%H:%M')

    msg_day_pattern = re.compile('on (\w.+)*,\s*(\w.+)*')
    msg_day_match =  msg_day_pattern.search(time_msg)
    if msg_day_match is None:
        print("none")
        msg_pattern = re.compile(',\s*(\w.+)*')
        msg_match = msg_pattern.search(time_msg)
        if msg_match is not None:
            msg = msg_match.group(1)
            return {"date": formatted_time, "msg": msg}
    else:
        msg_date = parser.parse(formatted_time + ' ' + msg_day_match.group(1)).strftime('%H:%M %B %d %Y')
        msg = msg_day_match.group(2)
        return {"date": msg_date, "msg": msg}



arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--msg", help="message to be sent. must be in this format: `[at HH:MM] on <date>, <msg here>. a time and/or date must be specified.")
args = arg_parser.parse_args()
msg = process_input(args.msg)
send(msg)

