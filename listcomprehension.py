# Example 1: Create a list of squared numbers for even numbers and cubed numbers for odd numbers
# Example 2: Create a list of 'even' or 'odd' based on the numbers in the original list
original_numbers = [1, 2, 3, 4, 5, 6]
result = [i**2 if i % 2 == 0 else i**3 for i in original_numbers]
result1 = ["even" if i % 2 == 0 else "odd" for i in original_numbers]
print(f"List of squared numbers for {original_numbers} is {result}")
print(f"List of even or odd numbers for {original_numbers} is {result1} ")
