import psu_term
import serial

DEFAULT_BAUD_RATE = 57600
DEFAULT_DATA_BITS = serial.EIGHTBITS
DEFAULT_STOP_BITS = serial.STOPBITS_ONE
DEFAULT_PARITY = serial.PARITY_NONE
DEFAULT_XONXOFF = True
DEFAULT_FLOW_CONTROL = None

UTF8 = 'utf-8'

DEBUG_PRINT = False

class psu():

    def __init__(self):
        comport_ls = psu_term.get_comports()
        comport_name = comport_ls[0].device
        self.serial_instance = serial.Serial(port=comport_name,
                                        baudrate=DEFAULT_BAUD_RATE,
                                        bytesize=DEFAULT_DATA_BITS,
                                        parity=DEFAULT_PARITY,
                                        stopbits=DEFAULT_STOP_BITS,
                                        xonxoff=DEFAULT_XONXOFF)

    def send_cmd(self, command):
        dec_strng = str(command + '\n')
        #unicode_cmd =
        psu_term.write_command(self.serial_instance, dec_strng)
