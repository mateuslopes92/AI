# stack lifo simulating browser stack
# s = []
# s.append("www.cnn.com/")
# s.append("www.cnn.com/world")
# s.append("www.cnn.com/india")
# s.append("www.cnn.com/china")

# pop remove and return the item
# print(s.pop())
# print(s)

# to get the last element without remove can use minus to get it
# print(s[-1])
# print(s)

from collections import deque
# stack = deque()
# stack.append("www.cnn.com/")
# stack.append("www.cnn.com/world")
# stack.append("www.cnn.com/india")
# stack.append("www.cnn.com/china")

# pop remove and return the item
# print(stack.pop())
# print(stack)

class Stack:
  def __init__(self):
      self.container = deque()

  def push(self,val):
      self.container.append(val)

  def pop(self):
      return self.container.pop()

  def peek(self):
      return self.container[-1]

  def is_empty(self):
      return len(self.container)==0

  def size(self):
      return len(self.container)

s = Stack()
s.push(5)
print(s)

print(s.peek())
print(s.pop())
print(s.is_empty())

s.push(5)
s.push(55)
s.push(56)
print(s.size())


