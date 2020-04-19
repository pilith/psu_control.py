import os
from psu_data import psu

PSU = psu()

def test_power_on:
    PSU.set_values(1, 48, 0.5)
    PSU.turn_on(1)
    os.system("pause")





