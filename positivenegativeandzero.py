# Write a Python Program to Check if a Number is Positive, Negative or Zero.
a = int(input("Enter a number : "))
if a > 0:
    print(f"Number you entered is {a} which is postive")
elif a == 0:
    print(f"Number you entered is {a} which is zero")
else:
    print(f"Number you entered {a} is negative")

# seconf way to do it
a = int(input("Enter a number : "))
message = f"Number you entered is {a} which is positive" if a > 0 else f"Number you entered is {a} which is zero" if a == 0 else f"Number you entered is {a} which is negative"
print(message)

# Write a Python Program to Check if a Number is Odd or Even.

a = int(input("Enter a number : "))
if a % 2 == 0:
    print(f"Number you entered is {a} which is even")
elif a % 2 == 1:
    print(f"Number you entered is {a} which is odd")
