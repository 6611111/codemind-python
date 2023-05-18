n=int(input())
s=0
b=n*n
while b!=0:
    r=b%10
    s=s+r
    b=b//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")