def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1

k=int(input())
l=0
m=0
c=0
for i in range(2,k):
    for j in range(i+1,k):
        if prime(i) and prime(j):
            if i*j==k:
                c+=1
                l=i
                m=j
                break
if c>0:
    print(l,m)
else:
    print(-1)