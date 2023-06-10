n=int(input())
lst=list(input().split())
res_l=[]
for i in lst:
    if i not in res_l:
        res_l.append(i)
for i in res_l:
    print(i,end=" ")