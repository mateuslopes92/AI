import time
import multiprocessing

square_result = []
def calc_square(numbers):
  print("calculate square numbers")
  for number in numbers:
    global square_result
    # time.sleep(5) # in case want to see in task manager add delay to make it slower
    print("square: ", number*number)
    square_result.append(number*number)

# def calc_cube(numbers):
#   print("calculate cube numbers")
#   for number in numbers:
#     # time.sleep(5) # in case want to see in task manager add delay to make it slower
#     print("cube: ",number*number*number)

if __name__ == "__main__":
  arr = [2, 3, 8, 9]
  p1 = multiprocessing.Process(target=calc_square, args=(arr,))
  # p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

  p1.start()
  # p2.start()

  p1.join() # wait till execution is over
  # p2.join() # wait till execution is over

  # will print empty array because every process has its own address space(virtual memory)
  # program variables are not shared between two processes, if want share data between two process
  # needs to use interprocess communication IPC
  print("result: ", square_result)
  print("Done!")