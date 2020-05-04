from numpy import random

#array =[]
def fillarray(ranges, N):
    set = []
    for n in N:
        for r in ranges:
            q = 0
            while q < 5:
                set.append(random.random_integers(0,r,n))
                q=q+1
        q = 0
        while q < 5:
            set.append(random.random_integers(0, n-1, n))
            q=q+1
        q =0
        while q < 5:
            set.append(random.random_integers(0, ranges[0], n))
            q = q + 1
    sorted(set,key=len)
    for i in set:
        for t in range(len(i)):
            int(i[t])
    return set
# array=fillarray([2**31, 2**15],[30000, 100000, 300000, 1000000])
# w = 1
# for i in array:
#     print ('%(number)d. %(length)d, %(max)d' % {"number": w,"length":len(i), "max": max(i)})
#     w = w+1








