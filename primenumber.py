import math
number = int(input("Enter your number: "))
Flag = True


if number == 1:
    Flag = False
else:
    for i in range(2, int(math.sqrt(number))+1):
        if number > 1 and number % i == 0:
            Flag = False
            break


if Flag:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
