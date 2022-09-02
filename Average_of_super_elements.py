n = int(input())
a = list(map(int,input().split()))
c = 0
s = 0
for i in set(a):
    if a.count(i)==i:
        c+=1
        s+=i
if c==0:
    print("-1")
else:
    su=s/c
    print("%.2f"%su)