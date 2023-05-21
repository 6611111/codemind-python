n=int(input())
flag=True
s=int(n**0.5)
for i in range(2,s+1):  
    if n%i==0:
        flag=False
        break
if flag==True:
    print("prime")
else:
    print("not a prime")