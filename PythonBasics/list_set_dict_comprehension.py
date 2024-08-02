# list comprehension provides a way to transform one list into another
numbers = [1, 2, 3, 4, 5, 6, 7]

# finding even numbers
even = []
# for i in numbers:
#   if i % 2 == 0:
#     even.append(i)
# print(even)

# with one line
even = [i for i in numbers if i % 2 == 0]
print(even)

# for SET
s = set([1, 2, 3, 4, 5, 6, 7])
evenSet = {i for i in s if i % 2 == 0}
print("SET even", evenSet)

# for dict
cities = ["mumbai", "new york", "paris"]
countries = ["india", "usa", "france"]

z = zip(cities, countries)
# for a in z:
#   print(a)

# makes pair key value
d = {city:country for city, country in zip(cities, countries)}
print(d)