n=int(input())
lst=list(input().split())
m=0
res=lst[0]
for i in lst:
    c=lst.count(i)
    if c>m:
        m=c
        res=i
print(res)