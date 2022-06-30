def happy(n):
    if n<10:
        return n
    
    r=0
    while n>0:
        r+=(n%10)**2
        n//=10
    return happy(r)
        
n=int(input())
if happy(n)==1 or happy(n)==7:
    print(True)
else:
    print(False)