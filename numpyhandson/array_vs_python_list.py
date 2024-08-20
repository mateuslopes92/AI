import numpy as np
import sys
import time

# numpy use less memory is more fast and convinient


# comparing size of array elements from numpy and python list
py_arr = range(1000)
# print(sys.getsizeof(5)*len(py_arr)) # 28000 bites | 1 element = 28bites

numpy_arr = np.arange(1000)
# print(numpy_arr.size*numpy_arr.itemsize) # 8000 bites | 1 element = 8bites



# List processing comparison
SIZE = 1000000

pl_1 = range(SIZE)
pl_2 = range(SIZE)

numpy_1 = np.arange(SIZE)
numpy_2 = np.arange(SIZE)

# python list
start = time.time()
result = [(x,y) for x, y in zip(pl_1, pl_2)]
print("python list took: ", (time.time() - start) * 1000) # 59.39507484436035

# numpy list
start = time.time()
result = numpy_1 + numpy_2
print("numpy took: ", (time.time() - start) * 1000) # 25.93207359313965