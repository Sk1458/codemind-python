def Ldig(n):
    R=0
    while(n>0):
        res=n%10
        n=n//10
        temp=n%10
        if res>temp:
            if res>R:
                R=res    
        else:
            if temp>R:
                R=temp
    return R
S=int(input())
print(Ldig(S))
    
            