from BlueFors_Alarm import *
import time


def start_alarm_system_test(pulse_tube_status, mc_temp, mc_channel_id=6, temp_threshold=0.05, wait_time=60):

    stop = False
    text_list = [""]
    email_list = get_email_list()

    slack_channel = "sneezy-bluefors"

    # Send message that the alarm system is activated
    Slacker = Slack_er()
    Slacker.send_message(slack_channel, '🚨 BlueFors Alarm was just activated!')

    while (not stop):

        pulse_tube_off = bool(pulse_tube_status == 0)
        mc_temp_high = bool(mc_temp >= temp_threshold)

        if pulse_tube_off or mc_temp_high:
            # Send message to Slack
            slack_message = '<!channel> ' + get_subject(pulse_tube_off, mc_temp_high, mc_temp)
            Slacker.send_message(slack_channel, slack_message)

            stop = True
            exit()

        time.sleep(wait_time)

if __name__ == "__main__":
    """
    TEST 1: Activated, then Pulse Tubes are Off
    """
    # pulse_tube_status = 0
    # mc_temp = 0.008
    # start_alarm_system_test(pulse_tube_status, mc_temp)

    """
    TEST 2: Nothing, then times out
    """
    # pulse_tube_status = 1
    # mc_temp = 0.008
    # start_alarm_system_test(pulse_tube_status, mc_temp)

    """
    TEST 3: Too hot
    """
    # pulse_tube_status = 1
    # mc_temp = 0.08
    # start_alarm_system_test(pulse_tube_status, mc_temp)

    """
    TEST 4
    """
    pulse_tube_status = 0
    mc_temp = 0.1
    start_alarm_system_test(pulse_tube_status, mc_temp)

    """
    TEST 5
    """
    # pulse_tube_status = 1
    # mc_temp = 0.1
    # start_alarm_system_test(pulse_tube_status, mc_temp)