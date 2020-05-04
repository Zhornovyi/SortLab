import random
#визначає оптимальний розподіл на підмасиви


def GetMiniRun(n):
    r = 0
    while n>=64:
        r = r|(n&1)
        n = n>>1
    return r+n


def InsSort(arr, start, end):
    for i in range(start + 1, end + 1):
        elem = arr[i]
        j = i - 1
        while j >= start and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr


def merge(arr, start, mid, end):
    if mid == end:
        return arr
    first = arr[start:mid + 1]
    last = arr[mid + 1:end + 1]
    len1 = mid - start + 1
    len2 = end - mid
    ind1 = 0
    ind2 = 0
    ind = start

    while ind1 < len1 and ind2 < len2:
        if first[ind1] < last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1

    while ind1 < len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1

    while ind2 < len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr


def TimSort(arr):
    n = len(arr)
    minrun = GetMiniRun(n)
    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        arr = InsSort(arr, start, end)

    curr_size = minrun
    while curr_size < n:
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            arr = merge(arr, start, mid, end)
        curr_size *= 2
    return arr


# def countingSort(unsortedList):
#     maxValue = 9
#     listLength = len(unsortedList)
#     k = len(str(max(unsortedList)))
#     output = [0] * (listLength)
#     while k>0 :
#         countList = [0] * (maxValue + 1)
#         for i in unsortedList:
#             q = i % 10
#             i -= q
#             countList[q] += 1
#         num_items_before =0
#         for i, count in enumerate(countList):
#             countList[i] = num_items_before
#             num_items_before += count
#
#         for i in unsortedList:
#             q = (i // 10 ** (k-1)) % 10
#             output[countList[q]] = output[countList[q]]*10 + q
#             countList[q] += 1
#         k -= 1
#
#     return output



def radix_sort(alist, base=10):
    if alist == []:
        return

    def key_factory(digit, base):
        def key(alist, index):
            return ((alist[index] // (base ** digit)) % base)

        return key

    largest = max(alist)
    exp = 0
    while base ** exp <= largest:
        alist = counting_sort(alist, base - 1, key_factory(exp, base))
        exp = exp + 1
    return alist


def counting_sort(alist, largest, key):
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[key(alist, i)] = c[key(alist, i)] + 1

    # Find the last index for each element
    c[0] = c[0] - 1  # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)
    for i in range(len(alist) - 1, -1, -1):
        result[c[key(alist, i)]] = alist[i]
        c[key(alist, i)] = c[key(alist, i)] - 1

    return result