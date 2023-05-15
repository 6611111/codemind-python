a=int(input())
b=a*a
s=0
while b!=0:
    r=b%10
    s=s+r
    b=b//10
if s==a:
    print("Neon Number")
else:
    print("Not Neon Number")