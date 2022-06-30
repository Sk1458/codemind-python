n = int(input())
arr = list(map(int,input().split()))
e = 0
o = 0
for i in range(0,n):
    if i%2==0:
        e+=arr[i]
    else:
        o+=arr[i]
if e>o:
    print(e-o)
else:
    print(o-e)