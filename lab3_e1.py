from DoublyLinkdedList import DoublyLinkedList
import random
import time

'''生成一个can'''
can = DoublyLinkedList()


'''初始化can，给can里加b个黑豆子，w个白豆子'''


def init(b, w):
    n = b
    m = w
    for i in range(0, n):
        can.insert_as_last(0)
    for j in range(0, m):
        can.insert_as_last(1)


'''按照规则取出和放回'''


def take_out_and_put_back():
    a = random.randint(1, can.size())
    c = can.get(a).data
    can.remove(a)
    b = random.randint(1, can.size())
    d = can.get(b).data
    can.remove(b)
    if c == d:
        can.insert_as_last(0)
    else:
        can.insert_as_last(1)


'''执行10次操作'''


def ten_times_play():
    total_bean()
    for i in range(0, 10):
        take_out_and_put_back()
        total_bean()


'''计算剩余黑豆子总数和白豆子总数'''


def total_bean():
    n = 0
    m = 0
    for i in range(1, can.size()+1):
        if can.get(i).data == 0:
            n += 1
        else:
            m += 1
    print('Black beans:', n, 'White beans:', m)


'''按照课件要求，初始黑豆子或白豆子分别取50-100，共51*51种组合，每个组合运行10次，输出实验结果'''
for k in range(50, 101):
    for l in range(50, 101):
        can.clear()
        init(k, l)
        ten_times_play()
        time.sleep(4)

