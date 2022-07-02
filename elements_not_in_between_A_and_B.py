n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
for i in range(n):
    if a[i]<x or a[i]>y:
        print(a[i],end=" ")
        c=1
if c==0:
    print("-1")