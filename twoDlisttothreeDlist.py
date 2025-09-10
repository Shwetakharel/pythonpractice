# Write a program that can convert a 2D list to 1D list
# Given 2D list
two_d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [j for i in two_d_list for j in i]
print(result)
