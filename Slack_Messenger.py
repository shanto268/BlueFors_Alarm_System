# -*- coding: utf-8 -*-
"""
===========================================
Program : BlueFors_Alarm_System/Slack_Messenger.py
===========================================
Summary:
Connects to Slack API and send messages
"""
__author__ = "Clark Miyamoto"


import slack
import os
from dotenv import load_dotenv


load_dotenv(".env")
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')


def connect_to_slack():
    '''
    Connects us to Slack API

    Args:
    token (str): 
    '''
    client = slack.WebClient(SLACK_TOKEN)

def send_message(channel, text):
    '''
    Sends a message to a specified channel w/ a specific message

    Args:
    channel (str): the channel in slack we want to contact (you don't need #)
    text (str): message you want to send to that channel
    '''
    client.chat_postMessage(channel=channel, text=text)

