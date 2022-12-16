t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    for i in range(1,n):
        if a[i-1]>a[i]:
            count+=1
    if count==0:
        print(count)
    else:
        print(max(a)-min(a))
    t-=1