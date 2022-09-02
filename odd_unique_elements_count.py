n = int(input())
a = list(map(int,input().split()))
c = 0
a = set(a)
a = list(a)
for i in range(len(a)):
    if a[i]%2:
        c+=1
print(c)