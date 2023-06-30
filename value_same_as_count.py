n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    c=lst.count(i)
    if i==c:
        if i not in l:
            l.append(i)
print(len(l))

        