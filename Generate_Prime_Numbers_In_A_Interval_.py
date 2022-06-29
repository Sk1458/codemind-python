def isprime(n):
    if n==1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        else:
            return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if isprime(i):
        print(i)