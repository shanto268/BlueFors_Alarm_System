from BlueFors_Alarm import *
import time


def start_alarm_system_test(pulse_tube_status, mc_temp, mc_channel_id=6, temp_threshold=0.05, wait_time=60):

    stop = False
    text_list = [""]
    email_list = get_email_list()

    while (not stop):

        pulse_tube_off = bool(pulse_tube_status == 0)
        mc_temp_high = bool(mc_temp >= temp_threshold)

        if pulse_tube_off or mc_temp_high:
            subject = get_subject(pulse_tube_off, mc_temp_high, mc_temp)
            content = get_content()
            Email = Emailer(email_list, text_list,
                    subjectLine=subject,
                    emailContent=content)
            Email.alert()
            stop = True
            exit()

        time.sleep(wait_time)

if __name__ == "__main__":
    """
    TEST 1
    """
    # pulse_tube_status = 0
    # mc_temp = 0.008
    # start_alarm_system_test(pulse_tube_status, mc_temp)

    """
    TEST 2
    """
    # pulse_tube_status = 1
    # mc_temp = 0.008
    # start_alarm_system_test(pulse_tube_status, mc_temp)

    """
    TEST 3
    """
    # pulse_tube_status = 1
    # mc_temp = 0.08
    # start_alarm_system_test(pulse_tube_status, mc_temp)

    """
    TEST 4
    """
    # pulse_tube_status = 0
    # mc_temp = 0.1
    # start_alarm_system_test(pulse_tube_status, mc_temp)

    """
    TEST 5
    """
    # pulse_tube_status = 1
    # mc_temp = 0.1
    # start_alarm_system_test(pulse_tube_status, mc_temp)

