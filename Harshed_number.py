x=int(input())
y=x
S=0
while(x>0):
    res=x%10
    S+=res
    x=x//10
if y%S==0:
    print("True")
else:
    print("False")
    
    
    

