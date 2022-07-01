k=int(input())
p=0
for i in range(1,k):
    if k%i==0:
        p+=i
if p==k:
    print("True")
else:
    print("False")    