class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)

        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def find(self, data):
        print('data:', data, 'self.data:', self.data)
        if data == self.data:
            print('Yes')
            return
        elif data < self.data:
            if self.left:
                self.left.find(data)
            else:
                print('No')
                return
        else:
            if self.right:
                self.right.find(data)
            else:
                print('No')
                return

    def delete(self, data):
        if data == self.data:
            if self.left is None and self.right is None:
                self.data = None
            elif self.left is None and self.right:
                self.data = self.right.data
                self.left = self.right.left
                self.right = self.right.right
            elif self.right is None and self.left:
                self.data = self.left.data
                self.right = self.left.right
                self.left = self.left.left
            else:
                if self.right.left is None:
                    self.data = self.right.data
                    self.right = None
                else:
                    m = self.right.left
                    while m.left is not None:
                        m = m.left
                    self.data = m.data
                    m = None
        elif data < self.data:
            if self.left:
                self.left.delete(data)
            else:
                return False
        else:
            if self.right:
                self.right.delete(data)
            else:
                return False


def eachlevelorder(Node, level, array):
    if Node is None or level < 1:
        return
    elif level == 1:
        array.append(Node.data)
    eachlevelorder(Node.left, level - 1, array)
    eachlevelorder(Node.right, level - 1, array)


def levelorder(Node):
    output = []
    array = []
    level = 1
    eachlevelorder(Node, level, array)
    output.append(array)
    level += 1
    while len(array) != 0:
        array = []
        eachlevelorder(Node, level, array)
        output.append(array)
        level += 1
    output.pop(len(output) - 1)
    print(output)


'''Example 1'''
r = Node(4)
r.insert(2)
r.insert(1)
r.insert(3)
r.insert(6)
r.insert(5)
r.insert(7)
levelorder(r)
r.delete(2)
r.delete(6)
levelorder(r)

'''Example 2'''
r = Node(1)
r.insert(2)
r.insert(3)
r.insert(4)
r.insert(5)
r.insert(6)
r.insert(7)
levelorder(r)
r.delete(2)
r.delete(6)
levelorder(r)
