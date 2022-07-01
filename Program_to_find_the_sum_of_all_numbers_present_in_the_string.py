s=input()
k="0123456789"
S=0
for i in s:
    if i in k:
        S+=int(i)
print(S)