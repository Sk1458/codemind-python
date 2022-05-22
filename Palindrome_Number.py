def rev(n):
    res=0
    while(n>0):
        rem=n%10
        res=res*10+rem
        n=n//10
    return res    

x=int(input())
for i in range(1,x+1):
    n=int(input())
    temp=n
    if rev(n)==temp:
        print("True")
    else:
        print("False")