n=int(input())
lst=list(map(int,input().split()))
l1=[]
l2=[]
for i in lst:
    c=lst.count(i)
    if(c==1):
        l1.append(i)
    elif c>1:
        l2.append(i)
if len(l2)==len(lst):
    print("-1")
else:
    print(*l1)