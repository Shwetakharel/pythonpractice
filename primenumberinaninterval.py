print("All the prime numbers in between 1 to 10 are : ")
for i in range(1, 11):
    if i > 1:
        for j in (2, i):
            if i % j == 0:
                break
            else:
                print(i)
