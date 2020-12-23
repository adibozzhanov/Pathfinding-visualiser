try:
    from tkinter import *
except:
    from Tkinter import *


class AlgTools:
    def __init__(self, master, r, c, bg="black", fg="white"):
        self.bg = bg
        self.fg = fg
        self.state = DISABLED
        self.choice = IntVar()
        self.setAlg = None

        self.master = master
        self.frame = Frame(self.master, bg=self.bg)
        self.frame.grid(row=r, column=c, sticky=W)
        self.title = Label(
            self.frame, text="Algorithm Control Tools: ", bg=self.bg, fg=self.fg)
        self.title.grid(row=0, column=0, sticky=W)

        self.checkBoxFrame = Frame(self.frame, bg=self.bg)
        self.checkBoxFrame.grid(row=2, column=0, sticky=W)
        self.options = [
            ("A*", 0),
            ("Dijkstra", 1)
        ]
        self.radioBoxes = []
        for option in self.options:
            self.radioBoxes.append(Radiobutton(self.checkBoxFrame, text=option[0], variable=self.choice, value=option[
                                   1], command=self.changeAlg, bg=self.bg, fg=self.fg, selectcolor="black", state=self.state))
        for each in self.radioBoxes:
            each.pack(anchor=W)

        self.buttonFrame = Frame(self.frame, bg=self.bg)
        self.buttonFrame.grid(row=1, column=0, sticky=W)
        self.buttonSet = ["Run", "Reset"]
        self.buttonPositions = [(2, 0), (1, 0)]
        self.buttons = []
        for i, each in enumerate(self.buttonSet):
            self.buttons.append(Button(
                self.buttonFrame, text=self.buttonSet[i], bg=self.bg, fg=self.fg, borderwidth=0, state=self.state))
            self.buttons[i].grid(row=self.buttonPositions[i]
                                 [0], column=self.buttonPositions[i][1], sticky=W)
        self.pathString = ""
        self.pathLabel = Label(self.frame, text = self.pathString, bg = self.bg, fg = self.fg)
        self.pathLabel.grid(row = 3, column = 0, sticky = W)

    def updatePathString(self, text):
        self.pathLabel.configure(text = text)


    def changeAlg(self):
        self.setAlg(self.choice.get())

        return





    def assignFunction(self,button, function):
        self.buttons[button].configure(command=function)

    def flipState(self):
        if self.state == NORMAL:
            self.state = DISABLED
        else:
            self.state = NORMAL
        for each in self.buttons:
            each.configure(state=self.state)
        for each in self.radioBoxes:
            each.configure(state = self.state)
