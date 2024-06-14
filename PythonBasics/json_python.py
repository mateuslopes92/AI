book = {}
book['tom'] = {
  'name': 'tom',
  'phone': 123131,
  'address': 'some address'
}
book['bob'] = {
  'name': 'bob',
  'phone': 123131,
  'address': 'some address'
}

import json
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "my_json")
s = json.dumps(book)

# creating a json file in same directory of this file
with open(file_path, "w") as f:
  f.write(s)
