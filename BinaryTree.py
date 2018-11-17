import TreeTraversal


class BinaryTree:
    def __init__(self, data=None):
        self.value = data
        self.LeftChild = None
        self.RightChild = None

    def add_left(self, data):
        self.LeftChild = BinaryTree(data)

    def add_right(self, data):
        self.RightChild = BinaryTree(data)


r = BinaryTree(1)
r.add_left(2)
r.add_right(3)
r.LeftChild.add_left(4)
r.LeftChild.add_right(5)

print('preorder:')
TreeTraversal.preorder(r)
print('inorder:')
TreeTraversal.inorder(r)
print('postorder:')
TreeTraversal.postorder(r)
print('levelorder:')
TreeTraversal.levelorder(r)
