import random


class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def swapup(self, i):
        while i//2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                tmp = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i//2

    def insert(self):
        self.heaplist.append(random.randint(1, 10))
        self.size += 1
        self.swapup(self.size)

    def swapdown(self, i):
        while i*2 <= self.size:
            mci = self.minchildindex(i)
            if self.heaplist[i] > self.heaplist[mci]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mci]
                self.heaplist[mci] = tmp
            i = mci

    def minchildindex(self, i):
        if i*2+1>self.size:
            return i*2
        elif self.heaplist[i*2] < self.heaplist[i*2+1]:
            return i*2
        else:
            return i*2+1

    def delete(self):
        self.heaplist[1] = self.heaplist[self.size]
        self.heaplist.pop()
        self.size -= 1
        self.swapdown(1)

t = 0
st = 0
tc = 0
schedule = BinHeap()

def timekeeper(stop):
    global t
    global st
    global tc
    if t % 3 == 0:
        schedule.insert()
        if schedule.size == 1:
            tc = schedule.heaplist[1]
    if schedule.size > 0 and t - st == tc:
        tc = schedule.heaplist[1]
        print(schedule.heaplist)
        schedule.delete()
        st = t
    if schedule.size > 0 and t % 5 == 0:
        print(schedule.heaplist)
        k = random.randint(1, schedule.size)
        schedule.heaplist[k] = random.randint(1, 10)
        schedule.swapup(k)
        schedule.swapdown(k)
    t += 1
    if t == stop:
        return
    else:
        timekeeper(stop)

timekeeper(50)
