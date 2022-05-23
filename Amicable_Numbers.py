x=int(input())
y=int(input())
S=0
D=0
for i in range(1,x):
    if x%i==0:
        S+=i
for j in range(1,y):
    if y%j==0:
        D+=j
if x==D and y==S:
    print("Amicable")
else:
    print("Not Amicable")
    
        