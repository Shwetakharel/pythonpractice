# Create 2 lists from a given list where
# 1st list will contain all the odd numbers from the original list and
# the 2nd one will contain all the even numbers
L = [1, 2, 3, 4, 5, 6]
odd_list = [o for o in L if o % 2 == 1]
even_list = [e for e in L if e % 2 == 0]
print(f"Odd list : {odd_list}")
print(f"Even list : {even_list}")


# Write a program to merge 2 list without using the + operator
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
L1.extend(L2)
print(L1)
