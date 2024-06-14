import os

# WRITE
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "my_text_file")

# first parameter is the path and second the mode
# mode can be r for read or w to write
# also can use a for append to file

# file = open(file_path, "w")
# file.write("Im learning python \nto do ai projects \nis awesome")
# file.close()

# READ
file = open(file_path, "r")

for line in file:
  tokens = line.split(' ')
  # print words in each line
  print(str(tokens))

file.close()

# also can be used with
# with open(file_path, "r") as file:
# do wheteaver you want here