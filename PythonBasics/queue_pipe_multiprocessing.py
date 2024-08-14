# sharing data between processes using array and value
import multiprocessing

# process number 2
def calc_square(numbers, square_result, value):
  value.value = 5.67
  for index, number in enumerate(numbers):
    square_result[index] = number*number

# process number 1
if __name__ == "__main__":
  arr = [2, 3, 8, 9]
  square_result = multiprocessing.Array('i', 3) # first parameter is data type i=integer d=double, second parameter is size
  value = multiprocessing.Value('d', 0.0) # first parameter is data type i=integer d=double, second parameter is size
  p = multiprocessing.Process(target=calc_square, args=(arr, square_result, value)) # pass the shared memory to the process

  p.start()
  p.join()

  print("outside process: ", str(square_result[:])) # with : we print all elements of the array
  print("outside process: ", str(value.value)) # with : we print all elements of the array