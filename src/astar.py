from constants import *
from field import *
import math
import time


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.prevNode = None
        self.state = None
        self.adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if self.x == 0:
            self.adjacent.remove((x - 1, y))
        if self.y == 0:
            self.adjacent.remove((x, y - 1))
        if self.x == COLUMNS - 1:
            self.adjacent.remove((x + 1, y))
        if self.y == ROWS - 1:
            self.adjacent.remove((x, y + 1))
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 1000000000
        self.traversable = True
        self.start = False
        self.end = False

    def g_calc(self):
        self.g_cost = self.prevNode.g_cost + 1

    def set_end(self):
        self.end = True

    def set_start(self):
        self.start = True
        self.state = "open"

    def is_traversable(self):
        return self.traversable

    def notTraversable(self):
        self.traversable = False

    def getCoords(self):
        return self.x, self.y

    def open(self):
        self.state = open

    def close(self):
        self.state = closed


class Astar:
    def __init__(self, field):
        self.f = field
        self.alg = 0
        self.start = None
        self.end = None
        self.nodes = [[Node(j, i) for j in range(COLUMNS)]for i in range(ROWS)]
        self.open = []
        self.closed = []
        self.current = None
        self.found = False
        self.path = []
        self.updatef = None
        self.log = None

    def min_f_node(self):
        return min(self.open, key=lambda x: x.f_cost)

    def update(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.get_node(j, i).state == "open":
                    self.f.setNode("open", j, i)
                if self.get_node(j, i).state == "closed":
                    self.f.setNode("closed", j, i)
        self.updatef()

    def reset(self):
        self.path = []
        self.open = []
        self.closed = []
        self.current = None

        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.f.getNode(j, i) == "open":
                    self.f.setNode("empty", j, i)
                if self.f.getNode(j, i) == "closed":
                    self.f.setNode("empty", j, i)
                if self.f.getNode(j, i) == "path":
                    self.f.setNode("empty", j, i)

        self.nodes = [[Node(j, i) for j in range(COLUMNS)]for i in range(ROWS)]
        self.found = False
        self.update()

    def init_map(self):
        self.reset()
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.f.getNode(j, i) == "wall":
                    self.nodes[i][j].notTraversable()
                if self.f.getNode(j, i) == "start":
                    self.nodes[i][j].set_start()
                    self.start = self.nodes[i][j]
                    self.open.append(self.nodes[i][j])
                if self.f.getNode(j, i) == "end":
                    self.nodes[i][j].set_end()
                    self.end = self.nodes[i][j]
        self.start.h_cost = self.h_cost(self.start)
        for i in range(ROWS):
            for j in range(COLUMNS):
                self.h_cost(self.get_node(j, i))

    def get_node(self, x, y):
        return self.nodes[y][x]

    def step(self):
        self.current = self.min_f_node()
        self.open.remove(self.current)
        self.closed.append(self.current)
        self.current.state = "closed"

        if self.current == self.end:
            return True
        else:
            for each in self.current.adjacent:
                neighbour = self.get_node(each[0], each[1])
                if (not neighbour.is_traversable()) or (neighbour in self.closed):
                    continue
                else:
                    predictedH = self.h_cost(neighbour)
                    predictedG = self.current.g_cost + 1
                    predictedF = predictedG + predictedH
                    if (predictedF < neighbour.f_cost):
                        neighbour.f_cost = predictedF
                        neighbour.g_cost = predictedG
                        neighbour.prevNode = self.current
                        if not(neighbour in self.open):
                            self.open.append(neighbour)
                            neighbour.state = "open"
            return False

    def loop_steps(self):
        k = 0
        self.init_map()
        while not self.found and len(self.open) > 0:
            k += 1
            self.found = self.step()
            if k % 15 == 0:
                self.update()
        self.update()
        if self.found == True:
            path = self.findPath(self.current)
            for each in self.path:
                self.f.setNode("path", each.x, each.y)
                self.update()
            self.log("Length: " + str(len(path)))
        else:
            self.log("Does Not Exist")
        self.f.setNode("start", self.start.x, self.start.y)
        self.f.setNode("end", self.end.x, self.end.y)

    def findPath(self, node):
        if node == self.start:
            self.path.append(node)
            node.state = "path"
            return self.path
        else:
            self.path.append(node)
            node.state = "path"
            return self.findPath(node.prevNode)

    def g_cost(self, node):
        x, y = node.getCoords()
        node.g_cost = abs(self.start.x - x) + abs(self.start.y - y)
        return node.g_cost

    def h_cost(self, node):
        if self.alg == 0:
            x, y = node.getCoords()
            node.h_cost = math.sqrt((self.end.x - x)**2 + (self.end.y - y)**2)
            #node.h_cost = abs(self.end.x - x) + abs(self.end.y - y)
            return node.h_cost
        if self.alg == 1:
            return 0

    def f_cost(self, node):
        node.f_cost = node.g_cost + node.h_cost
        return node.g_cost + node.h_cost

    def setAlg(self, choice):
        self.alg = choice


if __name__ == "__main__":
    f = Field()
    f.setNode("end", 5, 5)
    f.setNode("start", 0, 0)
    f.setNode("wall", 1, 1)

    a = Astar(f)
    a.init_map()
    print(list(map(lambda l: (l.x, l.y), a.loop_steps())))
