n=int(input())
lst=list(map(int,input().split()))
res=[]
for i in lst:
    if i not in res:
        if i%2!=0:
            res.append(i)
print(len(res))