def prime(n):
    if n==1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        else:
            return 1
            
x=int(input())
temp=x
if prime(temp)==1:
    while(x>0):
        res=x%10
        if prime(res)==0:
            print("Not Mega Prime")
            break
        x=x//10
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")
            
            
    