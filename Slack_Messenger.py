# -*- coding: utf-8 -*-
"""
===========================================
Program : BlueFors_Alarm_System/Slack_Messenger.py
===========================================
Summary:
Connects to Slack API and send messages
"""
__author__ = "Clark Miyamoto"


import asyncio
import os

import slack
from dotenv import load_dotenv
from slackeventsapi import SlackEventAdapter

from BlueFors import BlueFors

load_dotenv(".env")
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
# global mc_channel_id
mc_channel_id = 6
class Slack_er():

    def __init__(self, bf:BlueFors):
        self.client = slack.WebClient(SLACK_TOKEN)
        self.bf = bf
        self.slack_events_adapter = SlackEventAdapter(os.environ["SLACK_SIGNING_SECRET"], "/slack/events")

    def send_message(self, channel, text):
        '''
        Sends a message to a specified channel w/ a specific message

        Args:
        channel (str): the channel in slack we want to contact (you don't need #)
        text (str): message you want to send to that channel
        '''
        self.client.chat_postMessage(channel=channel, text=text)

    def listen_to_slack_events(self):
        @self.slack_events_adapter.on("message")
        def handle_message(event_data):
            message = event_data["event"]
            if message.get("subtype") is None and "status" in message.get('text', '') and f'<@{self.bot_user_id}>' in message.get('text', ''):
                self.send_status(message["channel"])

        self.slack_events_adapter.start(port=3000)

    def send_status(self, channel):
        pulse_tube_status = self.bf.get_pulse_tube_status()
        mc_temp = self.bf.get_temperature(mc_channel_id)
        status_message = f"Pulse Tube Status: {pulse_tube_status}\nMC Temperature: {mc_temp} K"
        print(status_message)
        self.client.chat_postMessage(channel=channel, text=status_message)

    @property
    def bot_user_id(self):
        return self.client.api_call("auth.test")["user_id"]