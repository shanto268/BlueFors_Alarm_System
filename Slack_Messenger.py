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

class Slack_er():

    def __init__(self):
        self.client = slack.WebClient(SLACK_TOKEN)

    def send_message(self, channel, text):
        '''
        Sends a message to a specified channel w/ a specific message

        Args:
        channel (str): the channel in slack we want to contact (you don't need #)
        text (str): message you want to send to that channel
        '''
        self.client.chat_postMessage(channel=channel, text=text)

