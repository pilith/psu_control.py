import serial
import serial.tools.list_ports

class psu():

    def __init__(self):
        self.serial_instance = serial.Serial(port=None,
                                        baudrate=57600,
                                        bytesize=serial.EIGHTBITS,
                                        parity=serial.PARITY_NONE,
                                        stopbits=serial.STOPBITS_ONE,
                                        xonxoff=True)

    def send_cmd(self, command):
        dec_strng = str(command + '\n')
        write_command(self.serial_instance, dec_strng)


def get_comports():
    comports = serial.tools.list_ports.comports
    comports_ls = comports()
    if not comports_ls:
        comports_ls = ['No Com Device', 'test1', 'test2']
    else:
        for port in comports_ls:
            comports_ls.append(port.device)
    return comports_ls


def write_command(serial_instance, unicode_str_to_write):
    """Write a command to the given serial instance."""

    UTF8 = 'utf-8'
    enc_str_to_write = unicode_str_to_write.encode(UTF8)
    something = serial_instance.write(enc_str_to_write)

    time.sleep(0.1)

