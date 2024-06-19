# ===== USING DICTIONARY ======
class HashTable:
  def __init__(self):
    self.MAX = 100
    self.arr = [None for i in range(self.MAX)]

  def get_hash(self, key):
    h = 0
    for char in key:
      # ord get the asc value
      h += ord(char)
    return h % self.MAX

  def add(self, key, value):
    h = self.get_hash(key)
    self.arr[h] = value

  def get(self, key):
    h = self.get_hash(key)
    return self.arr[h]

  # gives ability to use arr['key'] = value
  def __setitem__(self, key, value):
    h = self.get_hash(key)
    self.arr[h] = value

  # gives ability to use arr['key'] and will retrieve the value
  def __getitem__(self, key):
    h = self.get_hash(key)
    return self.arr[h]

  def __delitem__(self, key):
    h = self.get_hash(key)
    self.arr[h] = None

t = HashTable()
t.add("march 6", 300)
t["April 10"] = 150
print(t.get("march 6"))
# deleting element
# del t["April 10"]
print(t["April 10"])