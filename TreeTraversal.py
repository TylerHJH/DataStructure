def inorder(Node):
    if Node is None:
        return
    else:
        inorder(Node.LeftChild)
        print(Node.value)
        inorder(Node.RightChild)

def preorder(Node):
    if Node is None:
        return
    else:
        print(Node.value)
        preorder(Node.LeftChild)
        preorder(Node.RightChild)

def postorder(Node):
    if Node is None:
        return
    else:
        postorder(Node.LeftChild)
        postorder(Node.RightChild)
        print(Node.value)


def eachlevelorder(Node, level, array):
    if Node is None or level < 1:
        return
    elif level == 1:
        array.append(Node.value)
    eachlevelorder(Node.LeftChild, level - 1, array)
    eachlevelorder(Node.RightChild, level - 1, array)


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