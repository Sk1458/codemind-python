n=int(input())
r=0
while n:
    r=r*10+n%10
    n//=10
m=0
c=0
while r:
    if r%10==6 and c==0:
        m=m*10+9
        c=1
    else:
        m=m*10+r%10
    r//=10
print(m)