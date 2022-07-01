n=input()
c=0
c1=0
v='aeiou'
for i in range(0,len(n)):
    if n[i] in v:
        c1+=1
    if n[i] not in v:
        if c1>c:
            c=c1
        c1=0
if c1>c:
    c=c1
print(c)