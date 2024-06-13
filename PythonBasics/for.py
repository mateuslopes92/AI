exp=[2340, 2500, 2100, 3100, 2980]
total=0

for item in exp:
  total = total + item

print(total)

for i in range(1, 11):
  print(i)

for i in range(len(exp)):
  total = total + exp[i]

print(total)
# can use break or continue inside the for loop

# while
i = 1
while i<=5:
  print(i)
  i = i + 1