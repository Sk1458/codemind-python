n = int(input())
a = list(map(int,input().split()))
temp = a.copy()
temp.sort()
c = 0
for i in range(n):
    if a[i]!=temp[i]:
        c+=1
        ind = a.index(temp[i])
        a[i],a[ind]=a[ind],a[i]
print(c)