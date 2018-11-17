class FCNSTree:
    def __init__(self, data=None):
        self.value = data
        self.child = None
        self.sibling = None

    def insert_child(self, data):
        self.child = FCNSTree(data)

    def insert_sibling(self, data):
        self.sibling = FCNSTree(data)


r = FCNSTree(1)
r.insert_child(2)
r.child.insert_sibling(3)
r.child.insert_child(4)