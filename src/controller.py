try:
    from Tkinter import *
except:
    from tkinter import *


class Controller:
    def __init__(self, master, drawingTools, algTools, display, r, c):
        self.d = drawingTools
        self.a = algTools
        self.dis = display
        self.button = Button(master, text="Flip Controlls", command=self.flip)
        self.button.grid(row=r, column=c)

    def flip(self):
        self.d.flipState()
        self.a.flipState()
        self.dis.flipState()
