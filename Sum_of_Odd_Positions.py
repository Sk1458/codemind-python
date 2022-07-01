n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    if i%2:
        s+=a[i]
print(s)