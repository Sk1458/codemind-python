def add(n):
    a=0
    while n>0:
        r=n%10
        a+=r
        n=n//10
    return a
    
n=int(input())
while(n>10):
    n=add(n)
print(n)