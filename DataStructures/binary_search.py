from util import time_it

@time_it
def linear_search(numbers_list, number_to_find):
  for index, element in enumerate(numbers_list):
    if element == number_to_find:
      return index
  return -1

@time_it
def binary_search(numbers_list, number_to_find):
  left_index = 0
  right_index = len(numbers_list) - 1
  mid_index = 0

  while left_index <= right_index:
    # to divide numbers with simple slash we get float ex: 5/2 = 2.5
    # to get int we need double the slash so 5//2 = 2
    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
      return mid_index

    if mid_number < number_to_find:
      left_index = mid_index + 1
    else:
      right_index = mid_index - 1

  return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
  if right_index < left_index:
    return -1

  mid_index = (left_index + right_index) // 2
  if mid_index > len(numbers_list) or mid_index < 0:
    return -1

  mid_number = numbers_list[mid_index]

  if mid_number == number_to_find:
    return mid_index

  if mid_number < number_to_find:
    left_index = mid_index + 1
  else:
    right_index = mid_index - 1

  return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == '__main__':
  numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
  number_to_find = 45

  # just for performance test
  # linear_search took 2.435922622680664 mil sec
  # binary_search took 0.02002716064453125 mil sec
  # numbers_list = [i for i in range(10000001)]
  # number_to_find = 100000

  index_linear = linear_search(numbers_list, number_to_find)
  print(f"Number found at index {index_linear} using linear search")

  index_binary = binary_search(numbers_list, number_to_find)
  print(f"Number found at index {index_binary} using linear search")

  index_binary_recursive = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list) - 1)
  print(f"Number found at index {index_binary} using recursive binary search")