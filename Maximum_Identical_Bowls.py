n = int(input())
a = list(map(int,input().split()))
sm = sum(a)
for i in range(n,0,-1):
    if sm%i==0:
        print(i)
        break