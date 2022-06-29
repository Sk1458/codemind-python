def rev(n):
    res=0
    while n>0:
        rem=n%10
        res=res*10+rem
        n=n//10
    return res    

x=int(input())
X=x*x
y=rev(x)
Y=y*y
if X==rev(Y):
    print("True")
else:
    print("False")