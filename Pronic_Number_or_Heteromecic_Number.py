x=int(input())
for i in range(2,x):
    j=i-1
    if i*j==x:
        print("YES")
        break
else:
    print("NO")
        