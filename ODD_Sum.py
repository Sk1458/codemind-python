k=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,k):
    if a[i]%2:
        s+=a[i]
print(s)