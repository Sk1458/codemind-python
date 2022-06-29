x=int(input())
t=int(input())

while t:
    a,b=map(int,input().split())
    if a<x or b<x:
        print("UPLOAD ANOTHER")
    else:
        if a==b:
            print("ACCEPTED")
        else:
            print("CROP IT")
    t-=1