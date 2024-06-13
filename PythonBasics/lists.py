buy=["bread", "pasta", "fruits"]
print(buy)

item1=buy[0]
print(item1)

buy[0]="chips"
print(buy)

last=buy[-1]
print(last)

append=buy.append("butter")
print(buy)

#insert in location
buy.insert(1, "orange")
print(buy)

bathroom=["shampoo", "soap"]
merge=buy+bathroom
print(merge)

count=len(merge)
print(count)

contain="shampoo" in merge
print(contain)