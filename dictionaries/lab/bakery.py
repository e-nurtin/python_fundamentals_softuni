bakery_stock = input().split() # Take input as a string separated by single space

# bakery = {bakery_stock[i]: int(bakery_stock[i + 1])  # Using comprehension
#           for i in range(0,len(bakery_stock), 2)}

bakery = dict()  # Using standard cycle add the key if its not present, followed by value
for i in range(0, len(bakery_stock), 2):
    key = bakery_stock[i]
    value = bakery_stock[i + 1]
    bakery[key] = int(value)

print(bakery)
