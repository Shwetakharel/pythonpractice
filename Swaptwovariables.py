# Write a Python program to swap two variables.
a = 2
b = 3
print(f"Original value of a : {a} and b : {b}")
c = a
a = b
b = c
print(f"After swapping a : {a} and b : {b}")


# Write a Python program to swap two variables without temp variable.
a = 2
b = 3
a, b = b, a
print(a, b)
