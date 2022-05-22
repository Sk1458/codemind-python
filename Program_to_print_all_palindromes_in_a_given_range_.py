def rev(n):
    res=0
    while(n>0):
        rem=n%10
        res=res*10+rem
        n=n//10
    return res    
        
x=int(input())
y=int(input())
for i in range(x,y):
    if rev(i)==i:
        print(i,end=" ")