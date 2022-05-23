def rev(n):
    res=0
    while(n>0):
        rem=n%10
        res=res*10+rem
        n=n//10
    return res    

x=input()
L=len(x)
y=int(x)
z=y*y
res=0
for i in range(1,L+1):
    rem=z%10
    res=res*10+rem
    z=z//10
ans=rev(res)
if ans==y:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
