n,p=map(int,input().split())
temp=p
L=0
while temp:
    temp-=1
    L=L*10+n%10
    n//=10
revL=0
rev_n=0
first=0
while n:
    rev_n=rev_n*10+n%10
    n//=10
while L:
    revL=revL*10+L%10
    L//=10
while p:
    first=first*10+rev_n%10
    rev_n//=10
    p-=1
if first>revL:
    print(first-revL)
else:
    print(revL-first)