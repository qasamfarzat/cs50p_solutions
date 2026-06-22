parts = input("Fraction: ").split("/")
x = int(parts[0])
y = int(parts[1])
percentage = (x / y) * 100
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{round(percentage)}%")