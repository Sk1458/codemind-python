n = int(input())
L = []
for i in range(0,n):
    a = int(input())
    L.append(a)
c = int(input())
b = 0
for i in range(0,len(L)):
    if L[i]>c:
        b+=2
    else:
        b+=1
print(b)