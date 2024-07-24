try:
  raise MemoryError("Memory Error")
except MemoryError as e:
  print(e)

class Accident(Exception):
  def __init__(self, msg):
    self.msg = msg
  def print_exception(self):
    print("User defined exception")

try:
  raise Accident("Car crash")
except Accident as e:
  e.print_exception()

