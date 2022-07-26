# -*- coding: utf-8 -*-
"""
===========================================
Program : LFL_Lab_Maintenance/BlueFors_Alarm.py
===========================================
Summary: Sends out an email when pulse tubes are off
         or when the fridge's temperature is >= 50mK

         Launches program w/o GUI
"""
__author__ = "Clark Miyamoto"

from BlueFors import BlueFors
from Emailer import Emailer
import csv
import time
from Slack_Messenger import Slack_er

def get_subject(pt_off, mc_temp_high, temp):
    subject = []
    head_string = "[URGENT] "
    separator = ". "

    subject.append(head_string)
    if pt_off:
        subject.append("BlueFors' Pulse Tubes are OFF")
        subject.append(separator)
    if mc_temp_high:
        subject.append("BlueFors is WARM.")

    tail_string = " Current temperature is {} K".format(temp)
    subject.append(tail_string)

    subject = "".join(subject)
    return subject

def get_email_list():
    with open('emails.csv') as f:
        reader = csv.reader(f)
        email_list = list(reader)[0]
    return email_list

def get_content(content="This message has been automatically generated by BlueFors_Alarm script from LFL Emailer Bot."):
    return content


def start_alarm_system(folder_path, mc_channel_id=6, temp_threshold=0.05, wait_time=60) -> None:
    '''
    Call this function to start the alarm system.
    
    Args:
    - folder_path (str): path to 'BlueFors logs' folder. You can find this in the BlueFors app
    - mc_channel_id (int): Mixing Chamber Channel
    - temp_threshold (float): The temperature at which the alarm should go off in Kelvin
    - wait_time (int): Period of time we will wait to measure the fridge in seconds.

    Returns:
    - None
    '''

    bf = BlueFors('bf_fridge',
                folder_path=folder_path,
                channel_vacuum_can=1,
                channel_pumping_line=2,
                channel_compressor_outlet=3,
                channel_compressor_inlet=4,
                channel_mixture_tank=5,
                channel_venting_line=6,
                channel_50k_plate=1,
                channel_4k_plate=2,
                channel_magnet=None,
                channel_still=6,
                channel_mixing_chamber=5)

    stop = False
    text_list = [""]
    email_list = get_email_list()
    slack_channel = "sneezy-bluefors"

    # Send message that the alarm system is activated
    Slacker = Slack_er()
    Slacker.send_message(slack_channel, '🚨 BlueFors Alarm is now active!')

    while (not stop):

        pulse_tube_status = bf.get_pulse_tube_status()
        mc_temp = bf.get_temperature(mc_channel_id)

        print("Pulse Tube Status: {}".format(pulse_tube_status))
        print("MC Temperature: {} K".format(mc_temp))

        pulse_tube_off = bool(pulse_tube_status == 0)
        mc_temp_high = bool(mc_temp >= temp_threshold)

        
        if pulse_tube_off or mc_temp_high: #Triggers if something is wrong w/ fridge
            # Send out an email
            subject = get_subject(pulse_tube_off, mc_temp_high, mc_temp)
            content = get_content()
            Email = Emailer(email_list, text_list,
                    subjectLine=subject,
                    emailContent=content)
            Email.alert()

            # Send message to Slack
            slack_message = '<!channel> ' + get_subject(pulse_tube_off, mc_temp_high, mc_temp)
            Slacker.send_message(slack_channel, slack_message)

            stop = True
            exit()

        print("Waiting for next reading...")
        time.sleep(wait_time)




if __name__=='__main__':
    folder_path = r'C:\Users\lfl\Bluefors logs'
    start_alarm_system(folder_path)
