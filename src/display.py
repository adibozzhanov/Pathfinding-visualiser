try:
    from tkinter import *
except:
    from Tkinter import *
from constants import *


class Display:
    def __init__(self, master, field, width, height, r, c):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.grid(row=r, column=c)
        self.field = field
        self.mask = [[0 for i in range(ROWS)] for j in range(COLUMNS)]
        self.width = width
        self.height = height
        self.canvas = Canvas(self.frame, width=self.width, height=self.height)
        self.canvas.pack()
        self.state = NORMAL
        self.canvas.bind('<Motion>', self.update_mask)
        self.canvas.bind('<B1-Motion>', self.drawNode)

    def drawGrid(self):
        self.canvas.delete("all")
        for i in range(ROWS):
            for j in range(COLUMNS):
                x1 = j * (CELL_WIDTH + MARGIN)
                y1 = i * (CELL_HEIGHT + MARGIN)
                x2 = x1 + CELL_WIDTH
                y2 = y1 + CELL_HEIGHT
                if self.mask[i][j] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
                else:
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill=self.field.colorMap[self.field.getNode(j, i)], outline = "")
        self.master.update()

    def update_mask(self, mouse):
        if self.state == NORMAL:
            x, y = mouse.x, mouse.y
            x = x // (CELL_WIDTH + MARGIN)
            y = y // (CELL_HEIGHT + MARGIN)
            self.mask = [[0 for i in range(ROWS)] for j in range(COLUMNS)]
            if (mouse.x < CANVAS_WIDTH) and (mouse.y < CANVAS_HEIGHT) and (mouse.x >= 0) and(mouse.y >= 0):
                self.mask[y][x] = 1

    def drawNode(self, mouse):
        if self.state == NORMAL:
            self.mask = [[0 for i in range(ROWS)] for j in range(COLUMNS)]
            x, y = mouse.x, mouse.y
            x = x // (CELL_WIDTH + MARGIN)
            y = y // (CELL_HEIGHT + MARGIN)
            if self.field.getTool() == "start":
                for i in range(ROWS):
                    for j in range(COLUMNS):
                        if self.field.getNode(j, i) == "start":
                            self.field.setNode("empty", j, i)
            if self.field.getTool() == "end":
                for i in range(ROWS):
                    for j in range(COLUMNS):
                        if self.field.getNode(j, i) == "end":
                            self.field.setNode("empty", j, i)
            if (mouse.x < CANVAS_WIDTH) and (mouse.y < CANVAS_HEIGHT) and (mouse.x >= 0) and(mouse.y >= 0):
                self.field.setNode(self.field.getTool(), x, y)

    def flipState(self):
        if self.state == NORMAL:
            self.state = DISABLED
        else:
            self.state = NORMAL
        
