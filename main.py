from multiprocessing.context import Process
from init_input import fillarray
from RadixSort import RadixSort
from TimSort import TimSort
from IntroSort import IntroSort
from PartialSort import quicksort
from matplotlib import pyplot as plt
import numpy as np
import time
from multiprocessing import Manager
types = [30000, 100000, 300000, 1000000]
ranges = [2**31, 2**15]
def showQuick(res,queue):
    input_data = fillarray(ranges, types)
    results = []
    for i in range(0, len(input_data), 5):
        q = i
        start = time.perf_counter()
        while (q - i) < 5:
            quicksort(input_data[q], len(input_data[q]) / 2)
            q += 1
        print('%d q' % q)
        finish = time.perf_counter()
        results.append((finish - start) / 5)
    queue.append("Partial QuickSort")
    res.append(results)
def showIntro(res,queue):
    input_data = fillarray(ranges, types)
    results = []
    for i in range(0, len(input_data), 5):
        q = i
        start = time.perf_counter()
        while (q - i) < 5:
            IntroSort(input_data[q])
            q += 1
        print('%d i' % q)
        finish = time.perf_counter()
        results.append((finish - start) / 5)
    queue.append("IntroSort")
    res.append(results)
def showRadix(res,queue):
    input_data = fillarray(ranges, types)
    results = []

    for i in range(0, len(input_data), 5):
        q = i
        start = time.perf_counter()
        while (q - i) < 5:
            RadixSort(input_data[q])
            q += 1
        print('%d r' % q)
        finish = time.perf_counter()
        results.append((finish - start) / 5)
    queue.append("RadixSort")
    res.append(results)
def showTim(res,queue):
    input_data = fillarray(ranges, types)
    results = []
    for i in range(0, len(input_data), 5):
        q = i
        start = time.perf_counter()
        while (q - i) < 5:
            TimSort(input_data[q])
            q += 1
        print('%d t' % q)
        finish = time.perf_counter()
        results.append((finish - start) / 5)
    queue.append("TimSort")
    res.append(results)
def main():
    sequences = ['uniform 30k with 2^31', 'uniform 30k with 2^15', 'uniform 30k with 29999', 'normal 30k with 2^31',
                 'uniform 100k with 2^31', 'uniform 100k with 2^15', 'uniform 100k with 99999', 'normal 100k with 2^31',
                 'uniform 300k with 2^31', 'uniform 300k with 2^15', 'uniform 300k with 299999',
                 'normal 300k with 2^31', 'uniform 100k with 2^31', 'uniform 100k with 2^15',
                 'uniform 100k with 999999', 'normal 100k with 2^31']
    y_pos = np.arange(len(sequences))
    plt.rcdefaults()
    fig, ax = plt.subplots()
    colors = ['blue', 'green', 'orange', 'red']
    count = 0
    width = 0.4
    step = [-width/2, -width/4, width/2, width/4]
    with Manager() as manager:
        results = manager.list()
        queue = manager.list()
        Q = Process(target=showQuick, args=(results,queue))
        I = Process(target=showIntro, args=(results,queue))
        #R = Process(target=showRadix, args=(results,queue))
        T = Process(target=showTim, args=(results,queue))
        Q.start()
        I.start()
        #R.start()
        T.start()
        Q.join()
        I.join()
        #R.join()
        T.join()
        for i in results:
            ax.barh(y_pos+step[count], i, width/4, color=colors[count], label=queue[count])
            count += 1
        ax.set_yticks(y_pos)
        ax.set_yticklabels(sequences)
        ax.invert_yaxis()
        ax.set_xlabel('Час виконання')
        ax.set_title("Швидкость алгоритму для різних числових рядів")
        ax.legend()
        plt.show()

if __name__ == '__main__':
    main()








