n=int(input())
lst=list(map(int,input().split()))
l1=[]
l2=[]
f=1
for i in lst:
    c=lst.count(i)
    if i==c:
        if i not in l1:
            l1.append(i)
    elif i!=c:
        l2.append(i)
if len(lst)==len(l2):
    print("-1")
else:
    print(*l1)