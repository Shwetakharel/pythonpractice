s = input("Enter the string: ")
l = []
for i in s.split():
    l.append(i[0].upper() + i[1:].lower())

print(' '.join(l))
