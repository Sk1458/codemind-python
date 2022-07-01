n=int(input())
a=list(map(int,input().split()))
e=0
o=0
for i in range(n):
    if a[i]%2==0:
        e+=a[i]
    else:
        o+=a[i]
print(abs(e-o))