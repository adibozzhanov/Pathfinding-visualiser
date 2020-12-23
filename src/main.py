try:
    from tkinter import *
except:
    from Tkinter import *
from constants import *
from algTools import *
from drawTools import *
from display import *
from field import *
from controller import *
from astar import *
from maze import *
import time


if __name__ == "__main__":
    root = Tk()
    root.title("A*")
    root.configure(background=BACKGROUND)
    root.protocol("WM_DELETE_WINDOW", root.destroy)

    toolsFrame = Frame(root, bg=BACKGROUND)
    toolsFrame.grid(row=0, column=0, sticky=N)

    algTools = AlgTools(toolsFrame, 0, 0, BACKGROUND)

    drawField = Field()

    drawTools = DrawTools(toolsFrame, drawField, 1, 0, BACKGROUND)
    display = Display(root, drawField, CANVAS_WIDTH, CANVAS_HEIGHT, 0, 1)
    a = Astar(drawField)
    a.updatef = display.drawGrid
    algTools.assignFunction(1, a.reset)
    algTools.assignFunction(0, a.loop_steps)
    algTools.setAlg = a.setAlg
    a.log = algTools.updatePathString

    m = Maze(drawField)
    m.setUpdateFunction(display.drawGrid)
    drawTools.setMazeCommand(m.generate_maze)

    flip = Controller(toolsFrame, drawTools, algTools, display, 2, 0)
    while True:
        display.drawGrid()

    root.mainloop()
