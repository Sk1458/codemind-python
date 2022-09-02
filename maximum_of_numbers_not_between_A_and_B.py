n = input()
a = list(map(int,input().split()))
a1,a2 = map(int,input().split())
m = -1
for i in a:
    if i<a1 or i>a2:
        if m<i:
            m=i
print(m)