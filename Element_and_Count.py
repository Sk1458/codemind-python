n = int(input())
a = list(map(int,input().split()))
se = []
for i in a:
    if i not in se:
        se.append(i)
for i in se:
    print(i,a.count(i),end=" ")