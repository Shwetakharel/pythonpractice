# Print an inverted right-angled triangle (rows = 5):

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Print a number triangle (rows = 5):
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Print a triangle of row numbers (rows = 5):
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

# Print a reverse number triangle:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Print a pyramid of stars (rows = 5):
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

rows = 5
for i in range(1, rows+1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(1, i+1):
        print("*", end=" ")
    print()

# Print an inverted pyramid (rows = 5):
#  * * * * *
#  * * * *
#   * * *
#    * *
#     *
rows = 5
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
