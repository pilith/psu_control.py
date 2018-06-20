"""
this script acts as a little terminal
accepting commands from keyboard
forwarding them to CPX400DP psu over serial port
displaying responses

It helps testing commands for class in psu_serial_control.py
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time
import serial
import serial.tools.list_ports

DEFAULT_BAUD_RATE = 57600
DEFAULT_DATA_BITS = serial.EIGHTBITS
DEFAULT_STOP_BITS = serial.STOPBITS_ONE
DEFAULT_PARITY = serial.PARITY_NONE
DEFAULT_XONXOFF = True
DEFAULT_FLOW_CONTROL = None

UTF8 = 'utf-8'

DEBUG_PRINT = False


def get_comports():
    """Return the list of available com ports."""
    comports = serial.tools.list_ports.comports
    comport_list = comports()
    for com_port in comport_list:
        print(com_port.device)

    return comport_list


def write_command(serial_instance, unicode_str_to_write):
    """Write a command to the given serial instance."""
    enc_str_to_write = unicode_str_to_write.encode(UTF8)
    something = serial_instance.write(enc_str_to_write)

    if DEBUG_PRINT:
        print('{0} {1} {2} bytes written'.format(len(enc_str_to_write), enc_str_to_write, something))
    time.sleep(0.1)


def write_query_and_read_response(serial_instance, unicode_str_to_write):
    """Write a command and return the response."""
    write_command(serial_instance, unicode_str_to_write)
    time.sleep(0.1)
    resp = serial_instance.read(serial_instance.in_waiting)
#    resp = serial_instance.readline()
    return resp


def run():
    """Run the terminal."""
    comport_list = get_comports()
    if not comport_list:
        print('no device found')
        return

    comport_name = comport_list[0].device
    print('using {0}'.format(comport_name))

    serial_instance = serial.Serial(port=comport_name,
                                    baudrate=DEFAULT_BAUD_RATE,
                                    bytesize=DEFAULT_DATA_BITS,
                                    parity=DEFAULT_PARITY,
                                    stopbits=DEFAULT_STOP_BITS,
                                    xonxoff=DEFAULT_XONXOFF)

    while True:
        command = raw_input('cmd? ')
        unicode_command = unicode(command + '\n')
        if '?' in unicode_command:
            query_resp = write_query_and_read_response(serial_instance, unicode_command)
            print(query_resp.strip())
        else:
            write_command(serial_instance, unicode_command)


#if __name__ == '__main__':
#    run()
