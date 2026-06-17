word = input("camelCase: ")
result = ""
for char in word:
    if char.isupper():
        result += "_" + char.lower()
    else:
        result += char
print("snake_case:", result)