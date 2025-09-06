l = "abcabcmkabcabcmbabc"
s = "abc"
count = 0
for i in range(len(l) - len(s) + 1):
    if l[i:i+len(s)] == s:
        count += 1


print(count)
