def abdnt(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=i
    return c        
        


x=int(input())
temp=x
if abdnt(x)>temp:
    print("True")
else:
    print("False")
    