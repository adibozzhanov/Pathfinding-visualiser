

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.neighbours = []

    def search(self, data, parent=None):
        if self.data == data:
            return 1
        elif (len(self.neighbours) == 1) and (self.neighbours[0] == parent):
            return -1
        else:
            for kid in self.neighbours:
                if kid != parent:
                    if kid.search(data, self) == 1:
                        return 1
            return -1

    def addKid(self, kid):
        self.neighbours.append(kid)
        kid.neighbours.append(self)


if __name__ == "__main__":
    a = TreeNode(0)
    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    a.addKid(b)
    b.addKid(c)
    b.addKid(d)
    print(a.search(2))
