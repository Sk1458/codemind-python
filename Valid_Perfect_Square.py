x=int(input())
while(x>0):
    y=int(input())
    a=int(y**0.5)
    if y==a*a:
        print("True")
    else:
        print("False")
    x-=1    