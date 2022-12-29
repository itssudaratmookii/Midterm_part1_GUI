# Copyright (c) 2022 Sudarat Tokampang <sudaratto65@nu.ac.th>

""" Document string (Doc String)
A graphical user interface to observe sensor data
from a remote sensor through a matt communication channel
"""

__author__ = "Sudarat Tokampang"

# standard libra
import tkinter as tk
NAMES = ["Pick Rock", "Pick Scissor", "Pick Paper"]


class SensorUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.running = False
        self.button1 = tk.Button(self, text="Pick Rock",
                                command=self.button1_click)
        self.button1.pack(side=tk.TOP)

        self.button2 = tk.Button(self, text="Pick Scissor ",
                                command=self.button2_click)
        self.button2.pack(side=tk.TOP)

        self.button3 = tk.Button(self, text="Pick Paper ",
                                command=self.button3_click)
        self.button3.pack(side=tk.TOP)

        self.label = tk.Label(text="Your picked")
        self.label.pack(side=tk.TOP)


    def button1_click(self):
        """
        Toggle the stat of the sensor True -> False or False -> True,
        update the text of the run button, update the local StatusButton,
        and send the proper mqtt message
        """
        self.label.config(text="You picked Rock")

    def button2_click(self):
        self.label.config(text="You picked Scissor")

    def button3_click(self):
        self.label.config(text="You picked Paper")

if __name__ == "__main__":
    app = SensorUI()   # application a class ot tkinter.Tk
    # geometry is a method of the tkinter.Tk class that
    # sets the size of the app window. It takes a
    # string as on argument
    app.geometry("400x400")
    app.title('Rock Paper Scissor IoT game')
    app.mainloop()  # mainloop is method of tkinter.Tk
    # methods are function of classes
