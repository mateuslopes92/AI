# Colision
class HashTable:
  def __init__(self):
    self.MAX = 10
    self.arr = [[] for i in range(self.MAX)]

  def get_hash(self, key):
    h = 0
    for char in key:
      # ord get the asc value
      h += ord(char)
    return h % self.MAX

  # gives ability to use arr['key'] = value
  def __setitem__(self, key, value):
    h = self.get_hash(key)
    found = False
    for idx, element in enumerate(self.arr[h]):
      if len(element) == 2 and element[0] == key:
        self.arr[h][idx] = (key, value)
        found = True
        break

    if not found:
      self.arr[h].append((key, value))

  # gives ability to use arr['key'] and will retrieve the value
  def __getitem__(self, key):
    h = self.get_hash(key)
    for element in self.arr[h]:
      if element[0] == key:
        return element[1]

  def __delitem__(self, key):
    h = self.get_hash(key)
    for index, element in enumerate(self.arr[h]):
      if element[0] == key:
        del self.arr[h][index]

t = HashTable()
t["march 6"] = 120
t["march 6"] = 78
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459
print(t["march 6"])
print(t.arr)
print(t["march 17"])
del t["march 17"]
print(t.arr)
del t["march 6"]
print(t.arr)