def rev(n):
    res=0
    while(n>0):
        rem=n%10
        res=res*10+rem
        n=n//10
    return res

x=int(input())
y=x
while(1):
    y+=rev(y)
    if y==rev(y):
        print(y)
        break