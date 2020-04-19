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

    def open_ser(self, port):
        """Open serial port if it's not open already"""
        self.serial_instance.port = port

        if not self.serial_instance.isOpen():
            self.serial_instance.open()

    def turn_on(self, side):
        """Turn supplies on"""
        self.open_ser()
        self.send_cmd('op{} 1'.format(side))

    def turn_off(self, side):
        """Turn supplies  off"""
        self.open_ser()
        self.send_cmd('op{} 0'.format(side))

    def set_values(self, side, volt, amp):
        """Set voltage and current values of supply"""
        self.open_ser()
        self.send_cmd('V{} {}'.format(side, volt))
        self.send_cmd('I{} {}'.format(side, amp))

def get_comports():
    comports = serial.tools.list_ports.comports
    comports_ls = comports()
    comp_ls = []
    if not comports_ls:
        comp_ls = ['No Com Device', 'test1', 'test2']
    else:
        for port in comports_ls:
            comp_ls.append(port.device)
    return comp_ls


def write_command(serial_instance, unicode_str_to_write):
    """Write a command to the given serial instance."""

    UTF8 = 'utf-8'
    enc_str_to_write = unicode_str_to_write.encode(UTF8)
    something = serial_instance.write(enc_str_to_write)

    time.sleep(0.1)

