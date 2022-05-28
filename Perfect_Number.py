x=int(input())
c=0
for i in range(1,x):
    if x%i==0:
        c+=i
if x==c:
    print("True")
else:
    print("False")
    
        