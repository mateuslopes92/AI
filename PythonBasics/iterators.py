a = ["this", "is", "an", "array"]
# iterating over an array
for i in a:
  print(i)

# using dir(a) we can get all methods available for array
# using iter we can use the iteration which a for loop uses
# the code bellow has same result of the for loop trough the array
itr = iter(a)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

# implementing the iterator
class RemoteControl():
  def __init__(self):
    self.channels = ["hbo", "cnn", "espn"]
    self.index = -1

  def __iter__(self):
    return self

  def __next__(self):
    self.index += 1
    if self.index == len(self.channels):
      raise StopIteration
    return self.channels[self.index]

r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))