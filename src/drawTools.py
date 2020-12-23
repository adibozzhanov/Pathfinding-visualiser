try:
    from tkinter import *
except:
    from Tkinter import *

from constants import *


class DrawTools:
    def __init__(self, master, field, r, c, bg="black", fg="white"):
        self.bg = bg
        self.fg = fg
        self.state = NORMAL
        self.choice = IntVar()
        self.field = field
        self.master = master
        self.frame = Frame(self.master, pady=50, bg=self.bg)
        self.frame.grid(row=r, column=c, sticky=W)
        self.title = Label(self.frame, text="Drawing Tools",
                           bg=self.bg, fg=self.fg)
        self.title.grid(row=0, column=0, sticky=W)

        self.checkBoxFrame = Frame(self.frame, bg=self.bg)
        self.checkBoxFrame.grid(row=1, column=0, sticky=W)
        self.options = [
            ("Wall", 0),
            ("Eraser", 1),
            ("Start", 2),
            ("End", 3)
        ]
        self.radioBoxes = []
        for option in self.options:
            self.radioBoxes.append(Radiobutton(self.checkBoxFrame, text=option[0], variable=self.choice, value=option[
                                   1], command=self.out, bg=self.bg, fg=self.fg, selectcolor="black", state=self.state))
        for each in self.radioBoxes:
            each.pack(anchor=W)

        self.buttonFrame = Frame(self.frame, bg=self.bg)
        self.buttonFrame.grid(row=2, column=0, sticky=W)
        self.buttonSet = ["Clear", "Generate Maze"]
        self.buttonPositions = [(0, 0), (2,0)]
        self.buttons = []
        for i, each in enumerate(self.buttonSet):
            self.buttons.append(Button(
                self.buttonFrame, text=self.buttonSet[i], bg=self.bg, fg=self.fg, state=self.state))
            self.buttons[i].grid(row=self.buttonPositions[i]
                                 [0], column=self.buttonPositions[i][1], sticky=W)
        self.buttons[0].configure(command=self.clear)

    def setMazeCommand(self, function):
        self.buttons[1].configure(command = function)

    def out(self):
        if self.choice.get() == 0:
            self.field.setTool("wall")
        if self.choice.get() == 1:
            self.field.setTool("empty")
        if self.choice.get() == 2:
            self.field.setTool("start")
        if self.choice.get() == 3:
            self.field.setTool("end")

    def clear(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                self.field.setNode("empty", j, i)

    def flipState(self):
        if self.state == NORMAL:
            self.state = DISABLED
        else:
            self.state = NORMAL
        for each in self.buttons:
            each.configure(state=self.state)
        for each in self.radioBoxes:
            each.configure(state=self.state)
