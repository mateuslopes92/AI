# Queue FIFO with simple list
# stock_price_queue = []

# stock_price_queue.insert(0, 131.10)
# stock_price_queue.insert(0, 131.12)
# stock_price_queue.insert(0, 135)

# print(stock_price_queue)
# # print first in and remove it from the list
# print(stock_price_queue.pop())

# Queue with collections deque FIFO
from collections import deque

# USING DEQUE
# q = deque()
# q.appendleft(5)
# q.appendleft(8)
# q.appendleft(27)

# print(q)
# # print first in and remove it from the list
# print(q.pop())


# Using class
class Queue:
  def __init__(self):
    self.buffer = deque()

  def enqueue(self, val):
    self.buffer.appendleft(val)

  def dequeue(self):
    return self.buffer.pop()

  def is_empty(self):
    return len(self.buffer) == 0

  def size(self):
    return len(self.buffer)

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.buffer)
print(pq.dequeue())
print(pq.buffer)
print(pq.size())
print(pq.dequeue())
print(pq.dequeue())
print(pq.is_empty())