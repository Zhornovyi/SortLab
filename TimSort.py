def GetMiniRun(n):
    r = 0 #масив здвинутих бітів
    while n>=64:
        r = r|(n&1)# дадавання бітів
        n = n>>1# зсуваємо на одиничку
    return r+n

def InsertionSort(arr, start, end):
    for i in range(start + 1, end + 1):
        elem = arr[i] #обираємо елемент
        j = i - 1
        while j >= start and elem < arr[j]:#порівнюємо елемент  з попереднім доки не дойдем до початку
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr

def MergeSort(arr, start, mid, end):
    if mid == end:
        return arr
    first = arr[start:mid + 1]
    last = arr[mid + 1:end + 1]
    len1 = mid - start + 1
    len2 = end - mid
    ind1 = 0#вказівникн на преший масив
    ind2 = 0#вказівник на другий масив
    ind = start# ВКАЗІВНИК НА ВИХІДНИЙ МАСИВ

    while ind1 < len1 and ind2 < len2:
        if first[ind1] < last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1
    #якшо закінчується якась з частин то робота йде з якоюсь з частин
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
    n = len(arr)#20
    minrun = GetMiniRun(n)#5
    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)#знаходимо останный елемент мініран
        arr = InsertionSort(arr, start, end)#сортуємо масив вставками
    curr_size = minrun
    while curr_size < n:#процес злиття
        for start in range(0, n, curr_size * 2): #для 2 мініранів обєднуємо в один
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            arr = MergeSort(arr, start, mid, end)
        curr_size *= 2
    return arr