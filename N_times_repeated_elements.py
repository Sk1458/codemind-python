n = int(input())
a = list(map(int,input().split()))
k = int(input())
d = []
for i in range(n):
    if a.count(a[i])==k and a[i] not in d:
        d.append(a[i])
if len(d)==0:
    print("-1")
else:
    print(*d)