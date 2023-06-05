n=int(input())
sq=n*n
q=n
s=0
while(q!=0):
    r=q%10
    s=s*10+r
    q=q//10
k=s*s
o=0
while(k!=0):
    p=k%10
    o=o*10+p
    k=k//10
if o==sq:
    print("True")
else:
    print("False")