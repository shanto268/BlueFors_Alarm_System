# -*- coding: utf-8 -*-
"""
===========================================
Program : BlueFors_Alarm_System/GUI_Launcher.py
===========================================
Summary: Launches GUI version of BlueFors_Alarm.py

"""

from gooey import Gooey, GooeyParser
from BlueFors_Alarm import start_alarm_system

@Gooey(auto_start=True)
def main():
    """
    Auto-Lauches GUI

    Args:
    None

    Returns:
    None. Opens GUI.
    """
    parser = GooeyParser(description="BlueFors Alarm System")
    parser.parse_args()
    print('''BlueFors Alarm System is active. Keep this window open!
             If you want to turn off the alarm, close this window.''')
    
    start_alarm_system(folder_path)

if __name__=='__main__':
    folder_path = r'C:\Users\lfl\Bluefors logs'
    main()