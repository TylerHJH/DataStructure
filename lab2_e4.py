import time
import random

# 课件上的算法1
def max_subsequence_sum_n3(a, n):

    max_sum = 0
    for i in range(0, n):
        for j in range(i, n):
            this_sum = 0
            for k in range(i, j + 1):
                this_sum += a[k]
                if this_sum > max_sum:
                    max_sum = this_sum
    return max_sum


# 课件上的算法2
def max_subsequence_sum_n2(a, n):

    max_sum = 0
    for i in range(0, n):
        this_sum = 0
        for j in range(i, n):
            this_sum += a[j]
            if this_sum > max_sum:
                max_sum = this_sum
    return max_sum


# 课件上的算法4
def max_subsequence_sum_n(a, n):

    this_sum = max_sum = 0
    for j in range(0, n):
        this_sum += a[j]
        if this_sum > max_sum:
            max_sum =this_sum
        elif this_sum < 0:
            this_sum = 0
    return max_sum


# 课件上的算法3
def max_subsequence_sum_nlogn(a):

    # 定义递归结束标志
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return max(a[0], 0)

    # 将数组分为两个数组，则原问题的最大和=max(前半部分的最大和，后半部分的最大和，包含中间数的子数组的最大和)
    midx = int(len(a) / 2)
    a1 = a[:midx]
    a2 = a[midx:]

    # 计算包含中间数的子数组的最大和
    # 计算左半部分的最大和
    lmax = 0
    sum = 0
    for i in range(midx-1, -1, -1):
        sum += a[i]
        if sum > lmax:
            lmax = sum
    # 计算右半部分的最大和
    rmax = 0
    sum = 0
    for i in range(midx, len(a)):
        sum += a[i]
        if sum > rmax:
            rmax = sum
    mid_max = lmax + rmax # 含中间数的子数组的最大和 = 左半部分的最大和 + 右半部分的最大和

    return max(max_subsequence_sum_nlogn(a1), max_subsequence_sum_nlogn(a2), mid_max)


def build_arr(n):
    a = []
    for i in range(0, n + 1):
        a.append(random.randint(0, 10000))
    return a


def run(a):
    # 从快到满，从时间复杂度低到高挨个跑
    begin_time = time.process_time()
    print(max_subsequence_sum_n(a, len(a)))
    end_time = time.process_time()
    print('process time:', end_time - begin_time)

    begin_time = time.process_time()
    print(max_subsequence_sum_nlogn(a))
    end_time = time.process_time()
    print('process time:', end_time - begin_time)

    begin_time = time.process_time()
    print(max_subsequence_sum_n2(a, len(a)))
    end_time = time.process_time()
    print('process time:', end_time - begin_time)

    begin_time = time.process_time()
    print(max_subsequence_sum_n3(a, len(a)))
    end_time = time.process_time()
    print('process time:', end_time - begin_time)


a1 = build_arr(10)
a2 = build_arr(100)
a3 = build_arr(1000)
a4 = build_arr(10000)
a5 = build_arr(100000)

# 每次跑1个
# run(a1)
# run(a2)
# run(a3)
# run(a4)
run(a5)
