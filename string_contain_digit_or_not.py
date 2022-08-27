# program to display the no. of digits present in a given string

s=input()
c=0
for i in s:
    if i in "1234567890":
        c+=1
if c>0:
    print("Contains",c,"digit")
else:
    print("Doesn't contain digit")
        