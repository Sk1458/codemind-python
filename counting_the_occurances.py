#code to print the number of occurances of a particular character in a string

s=input()
a=input()
c=0
for i in s:
    if i in a:
        c+=1
if c>0:
    print(c)
else:
    print(-1)
                