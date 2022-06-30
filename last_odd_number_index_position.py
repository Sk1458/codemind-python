n=int(input())

a=list(map(int,input().split()))
i=0
for j in range(n):
    if a[j]%2:
        i=j
print(i)