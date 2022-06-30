n=int(input())
lp=2
rp=2
while lp*2<=n:
    lp*=2
while rp<=n:
    rp*=2
if n-lp<rp-n:
    print (n-lp)
elif n-lp==rp-n:
    print(n-lp,rp-n)
else:
    print(rp-n)