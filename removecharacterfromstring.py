a = input("Enter the string: ")
b = input("Enter the character that you want to remove : ")
result = ""
for i in a:
    if i != b:
        result += i

print(result)
