n=int(input())
lst=list(map(int,input().split()))
s1=0
s2=0
for i in range(len(lst)):
    if i%2!=0:
        s1=s1+lst[i]
    elif i%2==0:
        s2=s2+lst[i]
d=s1-s2
if d==0:
    print("YES")
else:
    print("NO")
