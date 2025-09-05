# Write a Python program to do arithmetical operations addition and division.

a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))
sum = a + b
print(f"Sum of {a} and {b} is {sum}")
if b == 0:
    print("Division cannot be performed")
else:
    divison = a / b
    print(f"Divison of {a}/ {b} is {divison}")
