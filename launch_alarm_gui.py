# -*- coding: utf-8 -*-
"""
===========================================
Program : BlueFors_Alarm_System/launch_alarm_gui.py
===========================================
Summary: Makes simple GUI to notify the program is on

"""

import easygui
import BlueFors_Alarm


folder_path =  r'C:\Users\lfl\Bluefors logs'
while True:
    BlueFors_Alarm.start_alarm_system(folder_path)
    easygui.msgbox('BlueFors Alarm System is Active. KEEP THIS WINDOW OPEN', 'BlueFors Alarm System', ok_button='Click here to turn off BlueFors Alarm')
    
    exit()


