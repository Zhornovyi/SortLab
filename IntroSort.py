import math
import sys
from heapq import heappush, heappop
def heapsort(arr):
    h = []
    for value in arr:
        heappush(h, value)
    result = []
    # витягення сортоварих есементів одиз за одним
    result = result + [heappop(h) for i in range(len(h))]
    return result
def InsertionSort(arr, begin , end):
    for i in range(begin + 1, end + 1):
        elem = arr[i] #обираємо елемент
        j = i - 1
        while j >= begin and elem < arr[j]:#порівнюємо елемент  з попереднім доки не дойдем до початку
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem

def Partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    #сортування
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i]) #swap
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1#повертає індекс елемента pivot

def MedianOfThree(arr, a, b, d):

    A = arr[a]
    B = arr[b]
    C = arr[d]

    if A <= B and B <= C:
        return b
    if C <= B and B <= A:
        return b
    if B <= A and A <= C:
        return a
    if C <= A and A <= B:
        return a
    if B <= C and C <= A:
        return d
    if A <= C and C <= B:
        return d

def IntrosortUtil(arr, begin, end, depthLimit):
    size = end - begin
    if size < 16:
        #починаємо сортування вставками якщо виділений масив менше 16 елементів
        InsertionSort(arr, begin, end)
        return
    if depthLimit == 0:
        # якщо досягнув ліміту глибини починається сортування кучою
        heapsort(arr)
        return
    pivot = MedianOfThree(arr, begin, begin + size // 2, end)#виділення pivon
    (arr[pivot], arr[end]) = (arr[end], arr[pivot])#свап елементів
    partitionPoint = Partition(arr, begin, end)# індекс де стоїть розподіл

    # сортування лівої та правої частини
    IntrosortUtil(arr, begin, partitionPoint - 1, depthLimit - 1)
    IntrosortUtil(arr, partitionPoint + 1, end, depthLimit - 1)


def IntroSort(unsorted):
    begin = 0
    end = len(unsorted)-1
    depthLimit = 2 * math.log2(end - begin)#визначення глибини
    IntrosortUtil(unsorted,begin, end, depthLimit)


# def printArr(arr):
#     print('Arr: ', arr)
# def main():
#     arr = [
#         2, 10, 24, 2, 10, 11, 27,
#         4, 2, 4, 28, 16, 9, 8,
#         28, 10, 13, 24, 22, 28,
#         0, 13, 27, 13, 3, 23,
#         18, 22, 8, 8]
#
#     n = len(arr)
#
#     Introsort(arr)
#     printArr(arr)
#
#
# if __name__ == '__main__':
#     main()