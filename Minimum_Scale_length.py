n=int(input())
a=list(map(int,input().split()))
m=a[0]
for i in a:
    if i<m:
        m=i
while m>0:
    c=0
    for i in a:
        if i%m==0:
            c+=1
    if c==n:
        print(m)
        break
    else:
        m-=1