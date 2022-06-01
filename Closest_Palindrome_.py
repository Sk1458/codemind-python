def rev(n):
    res=0
    while(n):
        rem=n%10
        res=res*10+rem
        n=n//10
    return res
    
k=int(input())
c=k
d=k
while(1):
    c+=1
    if c==rev(c):
        break
while(1):
    d-=1
    if d==rev(d):
        break
if c-k==k-d:
    print(d,c)
elif c-k>k-d:
    print(d)
elif c-k<k-d:
    print(c)
    

    
    