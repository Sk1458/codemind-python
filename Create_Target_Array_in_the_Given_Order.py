m = int(input())
list1 = list(map(int,input().split()))
n = int(input())
list2 = list(map(int,input().split()))
c = []
for i in range(m):
    c.insert(list2[i],list1[i])
print(*c)