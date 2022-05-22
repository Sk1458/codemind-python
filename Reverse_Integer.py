def rev(n):
    rem=0
    while(n>0):
        res=n%10
        rem=rem*10+res
        n=n//10
    return rem
def rrev(n):
    n=-n
    rem=0
    while(n>0):
        res=n%10
        rem=rem*10+res
        n=n//10
    return -rem
x=int(input())
if x>0:
    print(rev(x))
elif x<0:
    print(rrev(x))
    