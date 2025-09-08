s = input("Enter the string: ")
temp = ''
l = []
for i in s:
    if i != ' ':
        temp += i
    else:
        l.append(temp)
        temp = ''


if temp:
    l.append(temp)

count_string = len(l)
print(f"Frequency of string : {count_string}")
