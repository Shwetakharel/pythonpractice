# Checking odd even number
def is_oddeven(a):
    if a % 2 == 0:
        return "even"
    else:
        return "odd"


number = int(input("Enter the number: "))
result = is_oddeven(number)
print(f"The number you entered is {number} which is {result}")
