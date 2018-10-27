def cal_next(str):
    slen = len(str)
    nex = [-1] * slen
    k = -1
    for q in range(1, slen):
        while k > -1 and str[k + 1] != str[q]:
            k = nex[k]
        if str[k + 1] == str[q]:
            k += 1
        nex[q] = k
    return nex


def KMP(str, ptr):
    next = cal_next(ptr)
    find = []
    k = -1
    slen = len(str)
    plen = len(ptr)
    i = 0
    while i < slen:
        while k > -1 and ptr[k + 1] != str[i]:
            k = next[k]
        if ptr[k + 1] == str[i]:
            k += 1
        if k == plen - 1:
            find.append(i - plen + 1)
            i = i - plen + 1
            k = -1
        i += 1
    return find


next = cal_next('ababa')
print('next list:', next)
find = KMP('abadabababadbabaca', 'ababa')
print('Accuring times:', len(find), '\nPosition index:', find)