x=int(input())
z=1
while(x>0):
    y=int(input())
    for i in range(1,y+1):
        z*=i
    print(z) 
    x-=1
    z=1
    