import argparse

# we have 2 types of arguments Positional and Optional

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  # when use -- in front of parameter name will make optional
  # parser.add_argument("--number1", help="first number")
  # but to call needs to pass the name like
  # python3 argparse_python.py --number1 4
  parser.add_argument("number1", help="first number")
  parser.add_argument("number2", help="second number")
  parser.add_argument("operation", help="operation", choices=["add", "subtract", "multiply"])
  # to restrict user to only send valid parameters we can use choices

  args = parser.parse_args()

  print(args.number1)
  print(args.number2)
  print(args.operation)

  # if i run the program with -h will print the args like below:

  # usage: argparse_python.py [-h] number1 number2 operation

  # positional arguments:
  #   number1     first number
  #   number2     second number
  #   operation   operation

  # options:
  #   -h, --help  show this help message and exit


  # if i run passing the parameters will be like this: python3 argparse_python.py 4 5 add
  # the output:
  # 4
  # 5
  # add

  n1 = int(args.number1)
  n2 = int(args.number2)
  result = None
  if args.operation == 'add':
    result = n1 + n2
  elif args.operation == 'subtract':
    result = n1 - n2
  elif args.operation == 'multiply':
    result = n1 * n2
  else:
    print("unsupported operation")

  print("result is:", result)

