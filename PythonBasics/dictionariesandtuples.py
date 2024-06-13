phone_list={"jhon": 1232132, "joe": 12313654, "rob": 1321231}
print(phone_list)

# print specific
print(phone_list["jhon"])

# add
phone_list["joseph"]=545649
print(phone_list)

# delete
del phone_list["joseph"]
print(phone_list)

# desestruct can be for k,v in phone_list
for key in phone_list:
  print("key:", key, "value: ", phone_list[key])

jhon = "jhon" in phone_list
print(jhon)

# .clear cleans the dictionary