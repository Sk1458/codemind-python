# program to check if a given string is a palindrome string or not

t=int(input())
while t>0:
    s=input()
    if s[::-1]==s:
        if len(s)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
    t-=1    