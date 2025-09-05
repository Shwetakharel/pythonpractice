a = input("Enter the string: ")
flag = True
for i in range(len(a)//2):
    if a[i] != a[len(a) - i - 1]:
        flag = False
        print("Not a palindrome")
        break
if flag:
    print("Palindrome")
