def dis(n):
    i=1
    rev=0
    R=0
    while(n>0):
        res=n%10
        rev=rev*10+res
        n=n//10
    while(rev>0):
        res=rev%10
        R+=res**i
        rev=rev//10
        i+=1
    return R
x=int(input())
temp=x
if dis(x)==temp:
    print("True")
else:
    print("False")
        