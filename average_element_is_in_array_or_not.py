k=int(input())

a=list(map(int,input().split()))
A=sum(a)//k
if A in a:
    print(True)
else:
    print(False)