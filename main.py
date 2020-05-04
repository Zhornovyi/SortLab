from init_input import fillarray
from sorts  import TimSort, radix_sort
import timeit, numpy

# my_setup = "from init_input import fillarray"
# my_code = '''
# N = [30000, 100000, 300000, 1000000]
# ranges = [2**31, 2**15]
# arr = fillarray(ranges, N)
# '''
#
# print (timeit.timeit(setup=my_setup,stmt=my_code,number=10)/10)

types = [30000, 100000, 300000, 1000000]
ranges = [2**31, 2**15]
# input_data = fillarray(ranges, types)

array=fillarray(ranges,types)#всі згенеровані послідовності


unsort = [12, 45, 12, 23, 78, 56, 23]
output1 = radix_sort(unsort)
print(output1)





