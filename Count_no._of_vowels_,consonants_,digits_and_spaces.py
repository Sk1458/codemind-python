a=input().lower()
c,v,d,w=0,0,0,0
for i in a:
    if i in "aeiou":
        v+=1
    if i in "0123456789":
        d+=1
    if i in "bcdfghjklmnpqrstvwxyz":
        c+=1
    if i == " ":
        w+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)
