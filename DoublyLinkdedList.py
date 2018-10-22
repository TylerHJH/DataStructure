"""双向链表实现"""


"""节点类"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.pre = None
        self.next = None


"""双向链表"""


class DoublyLinkedList:
    """初始化"""
    def __init__(self):
        head = Node()
        tail = Node()
        self.head = head
        self.tail = tail
        self.head.next = self.tail
        self.tail.pre = self.head

    """获取长度"""
    def size(self):
        length = 0
        current = self.head
        while current.next != self.tail:
            length += 1
            current = current.next
        return length

    """在第一个位置插入"""
    def insert_as_first(self, data):
        node = Node(data)
        node.pre = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.pre = node

    """在最后一个位置插入"""
    def insert_as_last(self, data):
        node = Node(data)
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node
        node.pre.next = node

    '''获取节点位置'''
    def get_index(self, node_data):
        node = Node(node_data)
        index = 1
        current = self.head
        while current.next.data != node.data and current.next != self.tail:
            current = current.next
            index += 1
        if current.next == self.tail:
            print('NULL')
            return None
        else:
            return index

    '''获取首节点位置???????'''
    def first(self):
        index = self.get_index(self.head.next.data)
        return index

    '''获取末节点位置'''
    def last(self):
        index = self.get_index(self.tail.pre.data)
        return index

    '''查找元素'''
    def find(self, data):
        current = self.head
        while current.next.data != data and current.next != self.tail:
            current = current.next
        if current.next == self.tail:
            print('NULL')
            return None
        else:
            print('Exist')

    '''将新节点（数据）作为某节点（数据）后驱插入'''
    def insert_a(self, node_data, new_data):
        current = self.head
        while current.next.data != node_data and current.next != self.tail:
            current = current.next
        if current.next == self.tail:
            print('NULL')
            return None
        else:
            node = Node(new_data)
            node.pre = current.next
            node.next = current.next.next
            current.next.next = node
            node.next.pre = node

    '''将新节点（数据）作为某节点（数据）前驱插入'''
    def insert_b(self, node_data, new_data):
        current = self.head
        while current.next.data != node_data and current.next != self.tail:
            current = current.next
        if current.next == self.tail:
            print('NULL')
            return None
        else:
            node = Node(new_data)
            node.pre = current
            node.next = current.next
            current.next = node
            node.next.pre = node

    '''根据位置获取节点(非数据)'''
    def get(self, index):
        length = self.size()
        index = index
        current = self.head
        if index > length or index <= 0:
            print('OUT OF RANGE!')
            return None
        else:
            while index:
                current = current.next
                index -= 1
            return current

    '''删除节点'''
    def remove(self, index):
        node = self.get(index)
        if node:
            node.pre.next = node.next
            node.next.pre = node.pre

    '''判断非降序'''
    def disordered(self):
        current = self.head
        judgement = True
        if self.size() > 1:
            while judgement and current.next.next != self.tail:
                if current.next.data <= current.next.next.data:
                    current = current.next
                else:
                    judgement = False
            if judgement:
                print("List is disordered!")
            else:
                print("List is not disordered!")

    '''非降序排列'''
    def sort(self):
        n = self.size()
        for i in range(1, n):
            for j in range(1, n - i + 1):
                if self.get(j).data > self.get(j + 1).data:
                    temp = self.get(j).data
                    self.get(j).data = self.get(j + 1).data
                    self.get(j + 1).data = temp


    '''遍历所有'''
    def print_all(self):
        current = self.head
        while current.next != self.tail:
            print(current.next.data)
            current = current.next

    '''清空链表'''
    def clear(self):
        self.head.next = self.tail
        self.tail.pre = self.head