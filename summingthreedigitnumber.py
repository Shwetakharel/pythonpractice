number = int(input("Enter the number: "))
a = number % 10
number = number // 10
b = number % 10
number = number // 10
c = number
sum = a + b + c
print(f"Sum of 3 digits numbers is {sum}")
