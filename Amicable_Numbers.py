a=int(input())
b=int(input())
c1=0
c2=0
for i in range(1,a):
    if a%i==0:
        c1=c1+i
for j in range(1,b):
    if b%j==0:
        c2=c2+j
if c2==a and c1==b:
    print("Amicable")
else:
    print("Not Amicable")
        