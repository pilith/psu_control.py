#! python3
import psu_data
import tkinter as tk
from time import sleep

from tkinter import ttk


class Main_App(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        tk.Frame.__init__(self, self.root)

        self.powersupply = psu_data.psu()
        self.ser_port = tk.StringVar()
        self.root.title('PSU Control')
        self.create_widgets()

    def create_widgets(self):
        """Creating the buttons and labels for turning supply on and off"""

        # Frames for each supply
        self.com_frame = tk.LabelFrame(self.root, text='Com Port')
        self.left_frame = tk.LabelFrame(self.root, text='Left Supply', bg='green')
        self.right_frame = tk.LabelFrame(self.root, text='Right Supply', bg='red')
        self.both_frame = tk.LabelFrame(self.root, text='Synchronus On/Off')
        self.cycle_frame = tk.LabelFrame(self.root, text = 'Power Cycle')

        self.com_frame.pack(side='top')
        self.left_frame.pack(side='left', pady=5)
        self.right_frame.pack(side='right', pady=5)
        self.both_frame.pack(side='top')
        self.cycle_frame.pack(side='bottom')

        # Getting com ports to chose from
        self.com_menu = tk.OptionMenu(self.com_frame, self.ser_port, *psu_data.get_comports())
        self.com_menu.pack(side='top')

        # Voltage Reading and Setting
        self.left_voltframe = tk.LabelFrame(self.left_frame, text='Volt Amp')
        self.right_voltframe = tk.LabelFrame(self.right_frame, text='Volt Amp')
        self.left_voltframe.pack(side='top')
        self.right_voltframe.pack(side='top')

        # Left side voltage and amperage
        self.left_volt = tk.Entry(self.left_voltframe, width=4)
        self.left_amp = tk.Entry(self.left_voltframe, width=4)
        self.left_set = tk.Button(self.left_voltframe, text='SET', command=lambda: self.set_values('1'))
        tk.Label(self.left_voltframe, text='V\nA').pack(side='left')
        self.left_volt.pack(side='top')
        self.left_set.pack(side='right')
        self.left_amp.pack()

        # Right side voltage and amperage
        self.right_volt = tk.Entry(self.right_voltframe, width=4)
        self.right_amp = tk.Entry(self.right_voltframe, width=4)
        self.right_set = tk.Button(self.right_voltframe, text='SET', command=lambda: self.set_values('2'))
        tk.Label(self.right_voltframe, text='V\nA').pack(side='left')
        self.right_volt.pack(side='top')
        self.right_set.pack(side='right')
        self.right_amp.pack()

        # Buttons to turn on/off
        # lambda is needed to pass argument to function
        self.one_on_button = tk.Button(self.left_frame, text='On', command=lambda: self.turn_on('1'))
        self.one_on_button.pack()
        self.two_on_button = tk.Button(self.right_frame, text='On', command=lambda: self.turn_on('2'))
        self.two_on_button.pack()
        self.off_one = tk.Button(self.left_frame, text='Off', command=lambda: self.turn_off('1'))
        self.off_one.pack(side='bottom')
        self.off_two = tk.Button(self.right_frame, text='Off', command=lambda: self.turn_off('2'))
        self.off_two.pack(side='bottom')

        #Synch buttons
        self.dual_button_on = tk.Button(self.both_frame, text='Both On', command=lambda: self.dual_power('1'))
        self.dual_button_off = tk.Button(self.both_frame, text='Both Off', command=lambda: self.dual_power('0'))
        self.dual_button_off.pack(side='right')
        self.dual_button_on.pack(side='left')

        #Power cycling buttons
        self.cycle_time = tk.Entry(self.cycle_frame, width=4)
        tk.Label(self.cycle_frame, text = 'Time Off').pack(side='left')
        self.cycle_time.pack(side='right')
        self.cycle_button_l = tk.Button(self.cycle_frame, text='Left')
        self.cycle_button_r = tk.Button(self.cycle_frame, text='Right')

        self.cycle_button_l.anchor()
        self.cycle_button_r.anchor()
        
    def open_ser(self):
        """Open serial port if it's not open already"""
        self.powersupply.serial_instance.port = self.ser_port.get()

        if not self.powersupply.serial_instance.isOpen():
            self.powersupply.serial_instance.open()

    def turn_on(self, side):
        """Turn supplies on"""
        self.open_ser()
        self.powersupply.send_cmd('op{} 1'.format(side))

    def turn_off(self, side):
        """Turn supplies  off"""
        self.open_ser()
        self.powersupply.send_cmd('op{} 0'.format(side))

    def dual_power(self, state):
        """Turn on or off both supplies"""
        self.open_ser()
        self.powersupply.send_cmd(f'op1 {state}')
        self.powersupply.send_cmd(f'op2 {state}')

    #def power_cycle(self, side, time_off):
        
    def set_values(self, side):
        """Set voltage and current values of supply"""
        self.open_ser()
        if side == '1':
            v = self.left_volt.get()
            a = self.left_amp.get()
        else:
            v = self.right_volt.get()
            a = self.right_amp.get()
        self.powersupply.send_cmd('V{} {}'.format(side, v))
        self.powersupply.send_cmd('I{} {}'.format(side, a))

    def start(self):
        """start main loop"""
        self.root.mainloop()

if __name__ == "__main__":
    Main_App().start()
