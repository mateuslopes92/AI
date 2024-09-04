import numpy as np

array = np.array([5,6,9]) # normal array
array2 = np.array([[5,6,9], [1,2,3]]) # two dimensional array
print("dimension", array2.ndim) # print the dimension of the array in this case 2
print("dtype", array.dtype) # print the array type
print("itemsize", array.itemsize) # print the item size in this case 8 bites

arraytyped = np.array([5,6,9], dtype=np.float64) # defining the type of the data
print("dtype", arraytyped.dtype) # print the array type

print(arraytyped.size) # print the array size
print("shape", array2.shape) # print the array shape in columns and rows
print("reshape", array2.reshape(3, 2)) # print the array reshaped
print("flatten", array2.ravel()) # print the array in one dimension


print("zeros", np.zeros((3,4))) # create an array with zeros specified dimensions 3 rows and 4 columns
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

print("range", np.arange(1, 5)) # like the python range to create an array
print("range with steps", np.arange(1, 5, 2)) # like the python range to create an array the 3th parameter is the step

#can print max and min with
print("min", array.min())
print("max", array.max())
# to sum
print("sum", array.sum())
print("sum", array2.sum(axis=0)) # sum the column
print("sum", array2.sum(axis=1)) # sum the rows

# slicing
print("slice from beggin", array[0:2]) # slice the array
print("slice from end", array[-1]) # slice the array from the end, -1 print the last element



