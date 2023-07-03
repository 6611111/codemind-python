n=int(input())
lst=list(map(int,input().split()))
k=int(input())
l1=[]
l2=[]
for i in lst:
    c=lst.count(i)
    if c==k:
        if i not in l1:
            l1.append(i)
    elif c!=k:
        l2.append(i)
if len(lst)==len(l2):
    print("-1")
else:
    print(*l1)
        