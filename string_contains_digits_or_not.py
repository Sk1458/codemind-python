#program to identify if a given string has any numericals in it

t = int(input()) # for test cases
while t>0:
    s=input() 
    c=0 #flag
    for i in s:
        if i in "1234567890":
            c+=1
    if c==0:
        print("No")
    else:
        print("Yes")
    t-=1    
    

