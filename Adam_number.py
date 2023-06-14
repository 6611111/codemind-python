n=int(input())
sq=n*n
s=0
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
p=s*s
s1=0
while p!=0:
    q=p%10
    s1=s1*10+q
    p=p//10
if s1==sq:
    print("True")
else:
    print("False")