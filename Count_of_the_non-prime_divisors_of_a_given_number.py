def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

k = int(input())
c = 2
for i in range(2,(k//2)+1):
    if k%i==0:
        if prime(i):
            i+=1
            continue
        else:
            c+=1
print(c)