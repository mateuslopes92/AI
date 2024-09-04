import numpy as np

array = np.arange(12).reshape(3, 4)

# printing all items
for row in array:
  for cell in row:
    print(cell)

# without 2 for
for cell in array.flatten():
  print(cell)


# nditer
for c in np.nditer(array, order="C"):
  print(cell)


array2 = np.arange(3, 15, 4).reshape(3, 1)

#iterate over 2 arrays
for x, y in np.nditer([array, array2]):
  print(x, y)
