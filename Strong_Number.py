n=int(input())
c=1;
t=0;
q=n
while q!=0:
    r=q%10
    for i in range(1,r+1):
        c=c*i
    t=t+c
    c=1
    q=q//10
if t==n:
    print(F"The number {n} is a strong number")
else:
    print(f"The number {n} is not a strong number")