# Write a Python program to solve quadratic equation.
# The standard form of a quadratic equation is:
# where  a, b and c are real numbers and
# The solutions of this quadratic equation is given by:
# ax2 + bx + c = 0
# a ≠ 0
# # (−b ± sqrt(b2 − 4ac )/(2a)

import math as math
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c : "))

discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    x1 = (- b + math.sqrt(discriminant)) / (2 * a)
    x2 = (- b - math.sqrt(discriminant)) / (2 * a)
    print(f"Values of quadratic equation is {x1} and {x2}")
elif discriminant == 0:
    x1 = - b / (2 * a)
    print(f"Value of quadratic equation is {x1}")
else:
    real = - b/(2 * a)
    imaginary = math.sqrt(abs(discriminant))/(2 * a)
    print(f"Value of quadratic equation is : {real} + {imaginary}i")
    print(f"Value of quadratic equation is : {real} - {imaginary}i")
