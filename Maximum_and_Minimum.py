n=int(input())
lst=list(map(int,input().split()))
l1=[]
l2=[]
for i in lst:
    c=lst.count(i)
    if i==c:
        l1.append(i)
    elif i!=c:
        l2.append(i)
l1.sort()
if len(lst)==len(l2):
    print("-1")
else:
    print(l1[0],l1[len(l1)-1])