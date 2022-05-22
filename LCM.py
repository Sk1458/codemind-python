def lcm(a,b):
    if a>b:
        a,b=b,a
    c=a
    while True:
        if c%a==0 and c%b==0:
            return c
        c+=1



x,y=map(int,input().split())
print(lcm(x,y))
