#! python3
import psu_data
import tkinter as tk
from tkinter import ttk




class Main_App(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        tk.Frame.__init__(self, self.root)

        self.powersupply = psu_data.psu()
        self.root.title('PSU Control')
        self.create_widgets()

    def create_widgets(self):
        """Creating the buttons and labels for turning supply on and off"""

        # Frames for each supply
        self.one_frame = tk.LabelFrame(self.root, text='Left Supply', bg='green')
        self.two_frame = tk.LabelFrame(self.root, text='Right Supply', bg='red')
        self.one_frame.pack(side='left', padx=5, pady=5)
        self.two_frame.pack(side='right', padx=5, pady=5)

        #self.one_label = tk.Label(self.root, text='Supply One')
        #self.one_label.grid(row=0, column=0)
        #self.two_label = tk.Label(self.root, text='Supply Two')
        #self.two_label.grid(row=0, column=2)

        self.one_on_button = tk.Button(self.one_frame, text='On', command=self.turn1_on)
        self.one_on_button.pack(side= 'top')
        self.two_on_button = tk.Button(self.two_frame, text='On', command=self.turn2_on)
        self.two_on_button.pack(side='top')

        self.off_one = tk.Button(self.one_frame, text='Off', command=self.turn1_off)
        self.off_one.pack(side='bottom')
        self.off_two = tk.Button(self.two_frame, text='Off', command=self.turn2_off)
        self.off_two.pack(side='bottom')


        # Labels in top row
    def turn1_on(self):
        """Turns supply one on"""
        self.powersupply.send_cmd('op1 1')
    def turn2_on(self):
        """Turns supply two on"""
        self.powersupply.send_cmd('op2 1')
    def turn1_off(self):
        """Turns supply two off"""
        self.powersupply.send_cmd('op1 0')
    def turn2_off(self):
        """Turns supply two off"""
        self.powersupply.send_cmd('op2 0')

    def start(self):
        """start main loop"""
        self.root.mainloop()

if __name__ == "__main__":
    Main_App().start()
