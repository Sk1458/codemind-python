a = int(input())
b = int(input())
c = 0
for i in range(a,b+1):
    f = 0
    for j in range(i,b+1):
        f+=j
        if f%2:
            c+=1
print(c)