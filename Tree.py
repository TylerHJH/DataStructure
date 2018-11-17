class Tree:
    def __init__(self, data=None):
        self.value = data
        self.child = []

    def add(self, data):
        self.child.append(Tree(data))
