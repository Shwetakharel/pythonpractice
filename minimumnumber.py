a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
min = a
if b < a and b < c:
    min = b
elif c < a and c < b:
    min = c
else:
    pass


print(f"Minimum number among {a}, {b} and {c} is {min}")
