number = int(input("Enter a number : "))
result = ''
digit = '0123456789'


while number != 0:
    result = digit[number % 10] + result
    number = number // 10


print(result)
print(type(result))
