# Write a Python Program to Check Leap Year.
#  using a library

import calendar as cd

a = int(input("Enter the year : "))
if cd.isleap(a) == True:
    print(f"{a} is a leap year")
else:
    print(f"{a} is not a leap year")

# using a logic
a = int(input("Enter the year : "))
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(f"{a} is a leap year")
else:
    print(f"{a} is not a leap year")
