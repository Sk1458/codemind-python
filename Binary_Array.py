n = int(input())
a = list(map(int,input().split()))
e = a.count(0)
o = a.count(1)
if e+o==n:
    print(True)
else:
    print(False)