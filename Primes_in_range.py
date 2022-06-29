def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
    
x=int(input())
y=int(input())
a=0
while x<=y:
    if prime(x):
        a+=1
    x+=1
print(a)