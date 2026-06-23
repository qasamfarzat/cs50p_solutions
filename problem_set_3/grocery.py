groceries = {}

while True:
    try:
        item = input("Item: ").upper()
        groceries[item] = groceries.get(item, 0) + 1
    except EOFError:
        break

for item in sorted(groceries):
    print(groceries[item], item)