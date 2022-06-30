def prime(n):
    if n==1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        return 1
        
t=int(input())
for i in range(t):
    n=int(input())
    f,b=n,n
    while not prime(f) and not prime(b):
        f+=1
        b-=1
    if prime(f) and prime(b):
        print(min(f,b))
    elif prime(f):
        print(f)
    else:
        print(b)