n=int(input())
if n>=0:
    if n%2==0 or n%3==0 or n%5==0 or n==1:
        print("Ugly Number")
    else:
        print("Not Ugly Number")
else:
    print("Not Ugly Number")