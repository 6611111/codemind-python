n=int(input())
c_d=len(str(n))
s=0
q=n
while(q!=0):
    r=q%10
    s=s+r**c_d
    c_d=c_d-1
    q=q//10
if s==n:
    print("True")
else:
    print("False")