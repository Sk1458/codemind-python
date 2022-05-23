x=input()
L=len(x)
c=0
for i in range(0,L):
    for j in range(i+1,L):
        if x[i]==x[j]:
            c+=1
            break
           
if c>0:
    print("Not Unique Number")
else:
    print("Unique Number")
