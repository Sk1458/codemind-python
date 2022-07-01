def Neon(n):
    r=0
    while n>0:
        r+=n%10
        n//=10
    return r
n=int(input())
a=n*n
if n==Neon(a):
    print("Neon Number")
else:
    print("Not Neon Number")