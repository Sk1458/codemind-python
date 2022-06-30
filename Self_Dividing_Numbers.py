def slfd(n):
    temp=n
    while n>0:
        r=n%10
        if r==0 or temp%r!=0:
            return 0
        n//=10
    return 1
    
k=int(input())
l=int(input())
for i in range(k,l+1):
    if slfd(i):
        print(i,end=" ")