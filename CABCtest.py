import os
from time import sleep
from psu_data import psu

#PSU = psu()
#PSU.serial_instance.port = 'COM3'

def power_on_current():
    PSU = psu()
    PSU.serial_instance.port = 'COM3'
    PSU.set_values(1, 48, 0.5)
    PSU.turn_on(1)
    sleep(2)
    PSU.send_cmd('I1O?')
    #if float(PSU.current[0:5]) < 0.5:
    #    print('PASSED')
    #else:
    #    print('FAIL')
    PSU.turn_off(1)
    return float(PSU.current[0:5])

def test_power_on_current():
    assert power_on_current() < 0.5







