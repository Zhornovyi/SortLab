from numpy import random, round

def fillarray(ranges, N):
    set = []  # масив ексемплярів числових послідовновсей
    for n in N:
        for r in ranges:
            q = 0
            while q < 5:
                set.append(random.randint(0, r, n))  # генерація ряду випадкових чисел діапазону 2^31 та 2^15, рівномірний розплділ
                q = q + 1
        q = 0
        while q < 5:
            set.append(random.randint(0, n - 1,n))  # генерація ряду випадеових чисел діапазоном до n-1, рівномірний розподіл
            q = q + 1
        q = 0
        while q < 5:
            arr = round(random.normal(0, ranges[0], n))# генерація ряду випадкових чисел діапазону 2^31, нормальний розплділ
            arr = arr.astype(int)
            set.append(arr)
            q = q + 1
    sorted(set, key=len) #сортування множини екземплярів за довжиною ряду
    return set

#код перевірки
# array = fillarray([2 ** 31, 2 ** 15], [30000, 100000, 300000, 1000000])
# w = 1
# for i in array:
#     print('%(number)d. %(length)d, %(max)f' % {"number": w, "length": len(i), "max": max(i)})
#     w = w + 1
