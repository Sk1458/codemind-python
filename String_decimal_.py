#program to check if a given string is made of only decimals

t=int(input()) #testcases
while t>0:
    s = input()
    c=0
    for i in s:
        if i not in "1234567890":
            c+=1
    if c==0:
        print(True)
    else:
        print(False)
    t-=1    