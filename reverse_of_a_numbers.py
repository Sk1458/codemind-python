x=int(input())
res=0
while(x>0):
    rem=x%10
    res=res*10+rem
    x=x//10
print(res)    
    