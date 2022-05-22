def add(a,b):
    res=a+b
    return res

T=int(input())
for i in range(1,T+1):
    x,y=map(int,input().split())
    print(add(x,y))
    