#program to return index position of unique character in a given string

s = input()
a = s #duplicating the string
for i in s:
    c=0     # to check the count of a character in string 
    I=-1    # to have a note of j pointer's index position in for loop 
    for j in a:
        I+=1
        if i==j:
            c+=1
            if c==1:
                st = I # it stores the index postion
            if c>1:
                st=0   
    if c==1:
        print(st)
        break
if c>1:
    print(-1)

