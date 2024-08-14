# sharing data between processes using queue data structure
import multiprocessing

# process number 2
def calc_square(numbers, queue):
  for number in numbers:
    queue.put(number*number)

# process number 1
if __name__ == "__main__":
  arr = [2, 3, 8, 9]
  queue = multiprocessing.Queue()
  p = multiprocessing.Process(target=calc_square, args=(arr, queue)) # pass the shared memory queue to the process

  p.start()
  p.join()

  while queue.empty() is False:
    print(queue.get())
