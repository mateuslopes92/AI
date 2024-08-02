# set is an unordered collection of unique elements
basket = { "orange", "apple", "mango", "orange", "apple" }
print(type(basket))
print(basket) # output: {'mango', 'apple', 'orange'} without duplicates
# basket[0] dont work because sets dont works with indexes

# other way to initialize a set
a = set()
a.add(1)
a.add(2)
print(a) # {1, 2}

# works passing an collection as initializer
numbers = [1, 2, 3, 4, 2, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers) # {1, 2, 3, 4}

# frozen set is when you not able to change the content of the set
fs = frozenset(numbers)
# fs.add(5) # dont works


# sets support in operation
x = {"a", "b", "c"}
# "a" in x returns True
# "g" in x returns False

# iterating over the set
for i in x:
  print(i)

# union
y = {"a", "h", "g"}
print(x|y) # {'c', 'b', 'a', 'h', 'g'}

# intersection
print(x&y) # {'a'}

# difference
print(x-y) # {'b', 'c'}