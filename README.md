# reminder - A Python SMS Reminder System

## What it does
This is a Python command-line application that uses `at` and the Twilio API to send a reminder at a specified time. The purpose of this was to learn Python as well as create something I could actually use.

## How to use it
You must set the following environment variables ahead of time:
* `$TO_NUM`
* `$FROM_NUM`
* `$SID`: your Twilio SID
* `$TKN`: your Twilio token

The general format is this: `send_once.py --msg "at HH:mm, <message here>"`.
The time indicates when to send the message. Please note that the time must be in 24-hour format.
Example: `send_once.py --msg "at 13:00, eat lunch"`

This is a work in progress.
