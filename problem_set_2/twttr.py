s = input("Input: ")
for c in s:
    if c not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        print(c, end="")
print()