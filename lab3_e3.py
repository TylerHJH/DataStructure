"""7种排序"""
import time
import random

'''1.直接插入排序'''


def insert_sort(arr):
    # 直接插入排序
    for i in range(1,len(arr)):
        temp = arr[i]
        for j in range(i, -1, -1):
            if temp < arr[j - 1]:
                arr[j] = arr[j -1]
            else:
                break
        arr[j] = temp


'''2.希尔排序'''


def ShellInsetSort(array, len_array, dk):
    # 有gap的直接插入排序
    for i in range(dk, len_array):  # 从下标为dk的数进行插入排序
        position = i
        current_val = array[position]  # 要插入的数

        index = i
        j = int(index / dk)  # index与dk的商
        index = index - j * dk

        # while True:  # 找到第一个的下标，在增量为dk中，第一个的下标index必然 0<=index<dk
        #     index = index - dk
        #     if 0<=index and index <dk:
        #         break

        # position>index,要插入的数的下标必须得大于第一个下标
        while position > index and current_val < array[position-dk]:
            array[position] = array[position-dk]  # 往后移动
            position = position-dk
        else:
            array[position] = current_val


def shell_sort(array, len_array):
    # 希尔排序
    dk = int(len_array/2)  # 增量
    while dk >= 1:
        ShellInsetSort(array, len_array, dk)
        # print(array)
        dk = int(dk/2)


'''3.直接选择'''


def select_sort(arr):
    # 直接选择
    n = len(arr)
    for i in range(0, n):
        minIndex = i
        for j in range(i + 1, n):
            if arr[minIndex] > arr[j]:
                minIndex = j
        if i != minIndex:
            temp = arr[i]
            arr[i] = arr[minIndex]
            arr[minIndex] = temp


'''4.冒泡排序'''


def bubble_sort(arr):
    # 冒泡排序
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


'''5.快速排序'''


def quick_sort(array, left, right):
    # 快速排序
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


'''6.堆排序'''


def heap_sort(input_list):
    # 调整parent结点为大根堆
    def HeapAdjust(input_list, parent, length):

        temp = input_list[parent]
        child = 2 * parent + 1

        while child < length:
            if child + 1 < length and input_list[child] < input_list[child + 1]:
                child += 1

            if temp > input_list[child]:
                break
            input_list[parent] = input_list[child]
            parent = child
            child = 2 * child + 1
        input_list[parent] = temp

    if input_list == []:
        return []
    sorted_list = input_list
    length = len(sorted_list)
    # 最后一个结点的下标为length//2
    # 建立初始大根堆
    for i in range(0, length // 2 + 1)[::-1]:
        HeapAdjust(sorted_list, i, length)

    for j in range(1, length)[::-1]:
        # 把堆顶元素即第一大的元素与最后一个元素互换位置
        temp = sorted_list[j]
        sorted_list[j] = sorted_list[0]
        sorted_list[0] = temp
        # 换完位置之后将剩余的元素重新调整成大根堆
        HeapAdjust(sorted_list, 0, j)
        # print('%dth' % (length - j))
        # print(sorted_list)
    return sorted_list


'''7.归并排序'''


def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


'''测试'''


def build_arr(n):
    a = []
    for i in range(0, n + 1):
        a.append(random.randint(0, 10000))
    return a


a1 = build_arr(1000)
a2 = build_arr(10000)
a3 = build_arr(100000)


def time_insert_sort(list):
    begin = time.process_time()
    insert_sort(list)
    end = time.process_time()
    print(end - begin)


def time_shell_sort(list):
    begin = time.process_time()
    shell_sort(list,len(list))
    end = time.process_time()
    print(end - begin)


def time_select_sort(list):
    begin = time.process_time()
    select_sort(list)
    end = time.process_time()
    print(end - begin)


def time_heap_sort(list):
    begin = time.process_time()
    heap_sort(list)
    end = time.process_time()
    print(end - begin)


def time_bubble_sort(list):
    begin = time.process_time()
    bubble_sort(list)
    end = time.process_time()
    print(end - begin)


def time_quick_sort(list):
    begin = time.process_time()
    quick_sort(list, 0, len(list)-1)
    end = time.process_time()
    print(end - begin)


def time_merge_sort(list):
    begin = time.process_time()
    merge_sort(list)
    end = time.process_time()
    print(end - begin)

time_merge_sort(a1)
time_merge_sort(a2)
time_merge_sort(a3)
