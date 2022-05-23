def gcd(a,b):
    if(a<b):
            temp=a
            a=b
            b=temp
    c=a
    while True:
        if a%c==0 and b%c==0:
            return c
        c-=1        

x,y=map(int,input().split())
z=gcd(x,y)
print(z)