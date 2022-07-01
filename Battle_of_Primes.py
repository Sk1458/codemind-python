def prime(n):
    while n:
        c=0
        for i in range(2,n//2):
            if n%i==0:
                c+=1
        if c==0:
            return n
        n+=1
        
k=int(input())
l=int(input())
x=prime(k+l+1)
y=k+l
print(x-y)