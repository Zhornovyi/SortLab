from init_input import fillarray
from RadixSort import RadixSort
from TimSort import TimSort
from matplotlib import pyplot as plt
import numpy as np
import time

types = [30000, 100000, 300000, 1000000]
ranges = [2**31, 2**15]
test_data = [12, 45, 12, 23, 78, 56, 23, 35,65,76,14,57,87,65,12,16]
input_data = fillarray(ranges, types)
results = []

for i in range(0, len(input_data),5 ):
    q=i
    start = time.perf_counter()
    while (q-i)<5:
        TimSort(input_data[q])
        q+=1;
    finish = time.perf_counter()
    results.append((finish-start)/5)

sequences = ['uniform 30k with 2^31','uniform 30k with 2^15','uniform 30k with 29999','normal 30k with 2^31','uniform 100k with 2^31','uniform 100k with 2^15','uniform 100k with 99999','normal 100k with 2^31','uniform 300k with 2^31','uniform 300k with 2^15','uniform 300k with 299999','normal 300k with 2^31','uniform 100k with 2^31','uniform 100k with 2^15','uniform 100k with 999999','normal 100k with 2^31']
y_pos = np.arange(len(sequences))
error = np.random.rand(len(sequences))
plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh(y_pos, results, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(sequences)
ax.invert_yaxis()
ax.set_xlabel('Час виконання')
ax.set_title("Швидкость алгоритму для різних числових рядів")
plt.show()






