def rev(n):
    res=0
    while(n>0):
        rem=n%10
        res=res*10+rem
        n=n//10
    return res
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
    
x=int(input())
if prime(x):
    if prime(rev(x)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
        
    