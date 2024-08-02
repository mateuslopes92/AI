# simply way of creating iterator

def remote_control_next():
  yield "cnn"
  yield "espn"

# yield returns and preserve state of last execution
itr = remote_control_next()
print(itr)
print(next(itr))
print(next(itr))

# can iterate over an iterator too
for c in remote_control_next():
  print(c)