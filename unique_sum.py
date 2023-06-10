n=int(input())
lst=list(map(int,input().split()))
res_l=[]
for i in lst:
    if i not in res_l:
        res_l.append(i)
print(sum(res_l))