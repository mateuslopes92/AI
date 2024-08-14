import time
import threading

def calc_square(numbers):
  print("calculate square numbers")
  for number in numbers:
    time.sleep(0.2) # to take the cpu out of idle
    print("square: ", number*number)

def calc_cube(numbers):
  print("calculate cube numbers")
  for number in numbers:
    time.sleep(0.2) # to take the cpu out of idle
    print("cube: ",number*number*number)

arr = [2, 3, 8, 9]

t = time.time()
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join() # wait till t1 is done and go back to main thread
t2.join() # wait till t2 is done and go back to main thread

print("done in: ", time.time()-t)