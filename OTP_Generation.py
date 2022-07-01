k=input()
otp=""
for i in k:
    if int(i)%2!=0:
        otp+=str(int(i)**2)
print(otp)