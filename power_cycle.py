import subprocess
import serial
from time import sleep

PROG_FILE = 'coreboot_ABCx.rom'
FPGA_FILE = 'FA0010_CABC_EA-0256-RevJ.bin'

class Psu():

    def __init__(self):
        self.serial_instance = serial.Serial(port='com5',
                                        baudrate=57600,
                                        bytesize=serial.EIGHTBITS,
                                        parity=serial.PARITY_NONE,
                                        stopbits=serial.STOPBITS_ONE,
                                        xonxoff=True)

    def send_cmd(self, command):
        dec_strng = str(command + '\n')
        write_command(self.serial_instance, dec_strng)


def write_command(serial_instance, unicode_str_to_write):
    """Write a command to the given serial instance."""

    UTF8 = 'utf-8'
    enc_str_to_write = unicode_str_to_write.encode(UTF8)
    something = serial_instance.write(enc_str_to_write)

    sleep(0.1)


def psu_power(side, state, volt=0):
    powersupply.send_cmd(f'V{side} {volt}')
    powersupply.send_cmd(f'op{side} {state}')

powersupply = Psu()
if not powersupply.serial_instance.isOpen():
    powersupply.serial_instance.open()

x = 0
broken = False
while not broken:
    psu_power(2, 1, 19)
    sleep(10)
    psu_power(2, 0, 19)
    x = x + 1
    sleep(3)
    if x < 20:
        pass
    else:
        broken = True