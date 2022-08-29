#defanging an ip address

s = input()
a = ""
for i in s:
    if i in ".":
        a+="["
        a+=i
        a+="]"
    else:
        a+=i
print(a)        